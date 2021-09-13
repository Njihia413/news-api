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

@app.route('/business')
def business():
    '''
    View business page function that returns the business page and its data
    '''
    business = get_articles_depending_on_category('business')
    title = 'Business - Welcome to the best News Resource Website Online'
    return render_template('business.html',
                           title=title,
                           business=business
                           )


@app.route('/sports')
def sports():
    '''
    View sports page function that returns the sports page and its data
    '''
    sports = get_articles_depending_on_category('sports')
    title = 'Sports - Welcome to the best News Resource Website Online'
    return render_template('sports.html',
                           title=title,
                           sports=sports
                           )


@app.route('/entertainment')
def entertainment():
    '''
    View entertainment page function that returns the entertainment page and its data
    '''
    entertainment = get_articles_depending_on_category('entertainment')
    title = 'Entertainment - Welcome to the best News Resource Website Online'
    return render_template('entertainment.html',
                           title=title,
                           entertainment=entertainment
                           )


@app.route('/technology')
def technology():
    '''
    View technology page function that returns the technology page and its data
    '''
    technology = get_articles_depending_on_category('technology')
    title = 'Technology - Welcome to the best News Resource Website Online'
    return render_template('technology.html',
                           title=title,
                           technology=technology
                           )


@app.route('/health')
def health():
    '''
    View health page function that returns the health page and its data
    '''
    health = get_articles_depending_on_category('health')
    title = 'Health - Welcome to the best News Resource Website Online'
    return render_template('health.html',
                           title=title,
                           health=health
                           )


@app.route('/science')
def science():
    '''
    View science page function that returns the science page and its data
    '''
    science = get_articles_depending_on_category('science')
    title = 'Science - Welcome to the best News Resource Website Online'
    return render_template('science.html',
                           title=title,
                           science=science
                           )
