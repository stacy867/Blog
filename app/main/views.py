from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from flask_login import login_required,current_user
# from ..requests import get_movies,get_movie,search_movie
from .forms import BlogForm,CommentForm
from ..models import Writer,Blog,Comment

@main.route('/')
def index():
   
    
    blog=Blog.query.all()
    comment= Comment.get_comments(id)
    return render_template('index.html', current_user=current_user,blog=blog,comment=comment)

@main.route('/writer/<uname>')
def profile(uname):
    writer = Writer.query.filter_by(username = uname).first()

    if writer is None:
        abort(404)

    return render_template("profile/writer_profile.html", writer = writer)

@main.route('/writer/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if writer is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=writer.username))

    return render_template('profile/update.html',form =form)

@main.route('/newpost/', methods=['GET','POST'])
@login_required

def new_post():
    form = BlogForm()
    blog=Blog.query.all()
    writer = Writer.query.filter_by(writer_id = id).first()
    comment=Comment.query.filter_by(blog_id=id).first
    
    if form.validate_on_submit():
    
        new_post = Blog(title=form.title.data,content=form.content.data,author=form.author.data,writer_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        # flash('your post has been created!', 'success')
        return redirect(url_for('.index'))
    return render_template('newpost.html', title='New Post', blog_form=form,current_user=current_user,blog=blog,comment=comment,writer=writer)
        
@main.route('/newcomment/<int:id>',methods=['GET','POST'])

def new_comment(id):
    form =CommentForm()
    comment=Comment.query.filter_by(blog_id=id).all()
    # blog=Blog.query.all()
    blog=Blog.query.filter_by(id=id).first()
    title=f'write your comment'
    
    if form.validate_on_submit():
        new_comment=Comment(feedback=form.comment.data,blog_id=id)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    return render_template('comment.html',title=title,comment_form=form,blog=blog)
