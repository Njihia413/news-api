import urllib.request,json
from .models import Sources, Articles 
import os

#Sources = sources.Sources
#Articles = articles.Articles

#Getting api key
api_key = '3f35e79126c845a6a44ae14e6c47ba4a'

#Getting the news source base url
sources_base_url = None

#Getting the news articles base url
articles_base_url = None

def configure_request(app):
    global api_key,sources_base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    sources_base_url = app.config["NEWS_SOURCE_API_BASE_URL"]
    articles_base_url = app.config["NEWS_ARTICLES_API_BASE_URL"]


def get_sources():
    '''
    Function to get the json response to our url request
    '''
    get_sources_url = sources_base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)
        
    return sources_results

def process_sources_results(sources_list):
    '''
    Function that processes the sources results and transforms them into a list of objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns:
        sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(source_object)

    return sources_results

def get_articles(source_id): #Get articles using the source id
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(source_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def get_articles_from_source(source,pageSize): #Get news relating to a specific source and page size
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}&pageSize={}'.format(source,api_key,pageSize)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def get_articles_depending_on_category(category): #Get news depending on category
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(category, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    return articles_results 


def process_articles_results(articles_list):
    '''
    Function that processes the articles results and transform them into a list of objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns:
        articles_results: A list of articles objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results