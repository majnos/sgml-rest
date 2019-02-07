def to_list_view(article):
    return {
        'metadata': {
            'newid': article['metadata']['newid'],
            'oldid': article['metadata']['oldid'],
            'cgisplit': article['metadata']['cgisplit'],
            'lewissplit': article['metadata']['lewissplit'],
            'topics': article['metadata']['topics']
        },
        'fulltext':{
            'title': article['fulltext']['title'],
            'dateline': article['fulltext']['dateline'],
        },
        'topics': article['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics']   
    }

def to_detail_view(article):
    return {
        'metadata': {
            'newid': article['metadata']['newid'],
            'oldid': article['metadata']['oldid'],
            'cgisplit': article['metadata']['cgisplit'],
            'lewissplit': article['metadata']['lewissplit'],
            'topics': article['metadata']['topics']
        },
        'fulltext':{
            'title': article['fulltext']['title'],
            'dateline': article['fulltext']['dateline'],
            'body': article['fulltext']['body'],
        },
        'topics': article['fulltext']['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics']   
    }


    METADATA = {
  "newid",
  "oldid",
  "cgisplit",
  "lewissplit",
  "topics"
}

FULLTEXT = {
  "title",
  "dateline",
  "body"
}

LISTITEMS = {
  "places",
  "people",
  "orgs",
  "exchanges",
  "companies"
  "topics"
}