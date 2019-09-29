import json
import requests #responsible in making http requests visit geeksforgeeks
from .models import Quotes


base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']
    
def get_quotes():
    '''
    function that gets json response to our url requset
    '''
    quote_object=requests.get(base_url) #used to get the quote url
    new_quote =quote_object.json()#used in getting objects in json format
    author=new_quote.get("author")
    quote=new_quote.get("quote")
    object=Quotes(author,quote)
    return object
        
