from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Writer.query.get(int(user_id))


class Writer(UserMixin,db.Model):
    __tablename__='writers'
    
    id= db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog=db.relationship('Blog',backref="writers")
    
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
            

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
           
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
    
class Blog(db.Model):
    __tablename__="blogposts"
    
    id= db.Column(db.Integer,primary_key = True) 
    title= db.Column(db.String(255))
    content= db.Column(db.String(255))
    author=db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    writer_id=db.Column(db.Integer,db.ForeignKey('writers.id'))
    comment=db.relationship('Comment',backref="blogposts")  
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    # @classmethod
    # def clear_blogs(cls):
    #     Blog.all_blogs.clear()
        
    # display blogs
    
    def get_blogs(id):
        blogs = Blog.query.all()
        
        return blogs
class Comment(db.Model):
    __tablename__="comments"
    
    id = db.Column(db.Integer,primary_key =True)
    feedback= db.Column(db.String(255))  
    blog_id=db.Column(db.Integer,db.ForeignKey('blogposts.id'))
   
    
    
    def save_comment(self):
        '''
        function that saves comments
        '''
        db.session.add(self)
        db.session.commit() 
        
    @classmethod
    def get_comments(self,id):
        comment=Comment.query.filter_by(blog_id=id).all
        return comment    
               