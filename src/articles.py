import json
from schema import LISTITEMS, METADATA, FULLTEXT
from model import to_detail_view, to_list_view
from nested import getByDot
from flask import make_response, jsonify, render_template, abort
from errors import InvalidKey

class Articles:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.raw_data = json.load(f)

    def find_list(self, query={}):
        print('dummy_all:', query)
        return self.get_filtered_view(query)

    # def find_id(self, query={}):
    #     print('dummy_one', query)

    def get_filtered_view(self, query={}):
        try:
            output = []
            for article in self.raw_data:
                if self.match_article(article, query):
                    output.append(to_list_view(article))
            return output
        except KeyError:
            abort(404)

    # def get_filtered_detail(self, query):
    #     output = []
    #     for article in self.raw_data:
    #         if self.match_article(article, query):
    #             output.append(toDetailView(article))
    #     return output

    def match_article(self, article, query):
        for key in query:
            value = query[key]
            matched_key = self.add_prefix(key)
            if isinstance(getByDot(article, matched_key), list):
                if self.match_list(value, getByDot(article, matched_key)):
                    return True
                else:
                    return False
            elif isinstance(getByDot(article, matched_key), str):
                if self.match_single(value, getByDot(article, matched_key)):
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
        # if key in LISTITEMS:
        #     return 'listitems.'+key
        elif key in FULLTEXT:
            return 'fulltext.'+key
        else:
            return key

