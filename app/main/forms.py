
# from .forms import RegistrationForm,UpdateProfile
from .. import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
    
class BlogForm(FlaskForm):
    title = StringField('title', validators=[Required()])
    content = TextAreaField('content', validators=[Required()])
    author = TextAreaField('author', validators=[Required()])
    submit =  SubmitField('post')  
    
class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Leave a comment')   
        
    