from flask import Blueprint, render_template, redirect, url_for
from flask import request
import requests
from website import db
from .models import User, Task
import os
# from flask_login import login_required, current_user

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

def get_articles():
    articles = []
    url = ('https://newsapi.org/v2/everything?'
        'q=DeepSeek&'
        'sortBy=popularity&'
        'apiKey=' + NEWS_API_KEY)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
    
    return articles


@main_blueprint.route('/', methods=['GET', 'POST'])
# @login_required
def todo():    
    articles = get_articles()

    #return data
    return render_template('index.html', articles=articles)
