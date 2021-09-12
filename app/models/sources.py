class Sources:
    '''
    Sources class to define sources objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    '''
    id = Id of the sources e.g abc-news, bbc-news
    name = Name of the news source
    description = A short description of the news source
    url = Link to the news source page
    category = Category of the news source displayed e.g general, business, sports, technology....
    language = Language used to display the news source
    Country = Country where the news source has been fetched
    '''