from flask import render_template
from app import app
from .request import get_sources, get_articles, get_articles_from_source, get_articles_depending_on_category

#Views
@app.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    #Getting general news
    sources = get_sources()

    #Getting articles from various news sources
    bbc_news = get_articles_from_source('bbc-news','8')
    aljazeera_english = get_articles_from_source('al-jazeera-english','8')
    bbc_home_picture = get_articles_from_source('bbc-news','1')
    cnn = get_articles_from_source('cnn','2')
    google = get_articles_from_source('google-news','2')


    title = 'Home - Welcome to the best News Resource Website Online'
    return render_template('index.html',
    title = title,
    sources = sources,
    bbc_news = bbc_news,
    aljazeera_english = aljazeera_english,
    bbc_home_picture = bbc_home_picture,
    cnn = cnn,
    google = google)

@app.route('/source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page function that returns the articles page from a source
    '''
    articles = get_articles(source_id)
    print(articles)
    title = f'{source_id}'    
    return render_template(
        'articles.html',
        title = title,
        articles = articles)
