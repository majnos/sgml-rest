# separating to three APIs as requested by the task 
# input input could be also xml but it seems that json is more readable
# reading data just to the memory

from os.path import join, isfile, dirname
DEFAULT_FILE = join(dirname(__file__), '../json-data/reut2-000.json')

from flask import Flask, request, jsonify, make_response
import os
from articles import Articles
pwd = os.path.dirname(__file__) 
template_dir = os.path.join(pwd)


articles = Articles(DEFAULT_FILE)

app = Flask('Reuters REST', template_folder=template_dir)

@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'Error': 'Not Found'}), 404)  

@app.route('/reuters/articles', methods=['GET'])
def return_overview():
    return jsonify(articles.get_filtered_view(request.args))

@app.route('/reuters/search', methods=['GET'])
def return_fulltext():
    return jsonify(articles.get_fulltext_detail(request.args))

@app.route('/reuters/articles/<newId>', methods=['GET'])
def return_detail(newId):
    return jsonify(articles.get_filtered_detail(newId))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)