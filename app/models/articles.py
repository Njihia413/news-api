class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

        '''
        author = The one who wrote the article
        title = Title of the article
        description = A brief description of the article
        url = Link to the full article on the source website
        urlToImage = Article image
        publishedAt = Date the article was published
        content = Full and well detailed article 
        '''