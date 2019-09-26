from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required,current_user
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
   
    
    
    
    return render_template('index.html')
