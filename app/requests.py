import urllib.request,json
# from .models import Movie

# Getting api key
# api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    # api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']
