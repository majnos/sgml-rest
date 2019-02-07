# separating to three APIs as requested by the task 
# input input could be also xml but it seems that json is more readable
# reading data just to the memory

from os.path import join, isfile, dirname
DEFAULT_FILE = join(dirname(__file__), '../json-data/reut2-000.json')

from flask import Flask, request, jsonify, render_template
import os
from articles import Articles
# from errors import InvalidKey

articles = Articles(DEFAULT_FILE)

app = Flask('Reuters REST')

@app.route('/reuters/articles', methods=['GET'])
def return_overview():
    return jsonify(articles.get_filtered_view(request.args))

@app.route('/reuters/search', methods=['GET'])
def return_fulltext():
    return jsonify(articles.get_fulltext_detail(request.args))

@app.route('/reuters/articles/<newId>', methods=['GET'])
def return_detail(newId):
    return jsonify(articles.get_filtered_detail(newId))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)