from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
from ..models import Writer

@main.route('/')
def index():
   
    
    
    
    return render_template('index.html')

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