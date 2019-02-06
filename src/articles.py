import json

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
            if self.match_article(self.raw_data, query):
                output.append(article)
        return output

    def match_article(self, article, query):
        for key in query:
            value = query[key]
 #           if self.match_single(self.raw_data[query_key], query_value) or self.match_list(query_value, self.raw_data[query_key]):
            if self.match_single(self.raw_data[key], value):                
                return True
            else:
                return False
            
    def match_single(self, item1, item2):
        if (item1 == item2):
            return True
        else:
            return False

    def match_list(self, item1, item2):
        if (item1 in item2):
            return True
        else:
            return False