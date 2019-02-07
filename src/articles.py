import json
from schema import LISTITEMS, METADATA, FULLTEXT

class Articles:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.raw_data = json.load(f)
    
    def find_list(self, query={}):
        print('dummy_all:', query)
        return self.filter_articles(query)

    def find_id(self, query={}):
        print('dummy_one', query)

    def filter_articles(self, query):
        output = []
        for article in self.raw_data:
            if self.match_article(article, query):
                listModel = ListModel(article)
                output.append(ModelArticle)
        return output

    def match_article(self, article, query):
        for key in query:
            value = query[key]
            matched_key = self.add_prefix(key)
 #           if self.match_single(self.raw_data[query_key], query_value) or self.match_list(query_value, self.raw_data[query_key]):
            if self.match_list(value, article[key]):                
                return True
            else:
                return False
            
    def match_single(self, item1, item2):
        if (item1 == item2):
            return True
        else:
            return False

    def match_list(self, item, list):
        if (item in list):
            return True
        else:
            return False
    
    def add_prefix(self, key):
        if key in METADATA:
            return 'metadata.'+key
        if key in LISTITEMS:
            return 'listitems.'+key
        if key in FULLTEXT:
            return 'fulltext.'+key

