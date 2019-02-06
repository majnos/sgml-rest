import json

class Articles:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.json = json.load(f)
    
    def find_all(self, query={}):
        print('dummy_all', query)

    def find_one(self, query={}):
        print('dummy_one', query)
