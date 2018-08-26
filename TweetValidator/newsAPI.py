from newsapi import NewsApiClient

searchstring = "Fake news"

api = NewsApiClient(api_key='')
api.get_everything(q=searchstring)
api.get_sources()