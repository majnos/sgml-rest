from os.path import join, isfile, dirname
DEFAULT_FILE = join(dirname(__file__), '../json-data/reut2-000.json')

from flask import Flask, request, jsonify
import os
from articles import Articles

articles = Articles(DEFAULT_FILE)

app = Flask('Reuters REST')

@app.route('/reuters/articles', methods=['GET'])
def return_overview():
    return jsonify(articles.find_list(request.args))

@app.route('/reuters/search', methods=['GET'])
def return_fulltext():
    return jsonify(articles.find_text(request.args))

@app.route('/reuters/articles/<id>', methods=['GET'])
def return_detail(id):
    return jsonify(articles.find_id(id))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port, debug=True)
