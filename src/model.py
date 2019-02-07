def toListView(article):
    return {
        'newId': article['newId'],
        'oldId': article['oldId'],
        'cgisplit': article['cgisplit'],
        'lewissplit': article['lewissplit'],
        'topics': article['topics'],
        'title': article['title'],
        'dateline': article['dateline'],
        'topics': article['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics']   
    }

def toDetailModel(article):
    return {
        'newId': article['newId'],
        'oldId': article['oldId'],
        'cgisplit': article['cgisplit'],
        'lewissplit': article['lewissplit'],
        'topics': article['topics'],
        'title': article['title'],
        'dateline': article['dateline'],
        'body': article['body'],
        'topics': article['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics']   
    }    