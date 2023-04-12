from flask import Flask, jsonify, request
from scraper import  (
    search_mercadolivre_by_category, 
    search_buscape_by_category, 
    search_mercadolivre_by_keyword, 
    search_buscape_by_keyword, 
    search_all, 
    )

app = Flask(__name__)


@app.route('/search_meli_by_category', methods=['GET'])
def search_mercadolivre_category():
    category = request.args.get('category')
    results = search_mercadolivre_by_category(category)
    return jsonify(results)


@app.route('/search_meli_by_keyword', methods=['GET'])
def search_mercadolivre_keyword():
    category = request.args.get('category')
    keyword = request.args.get('keyword')
    results = search_mercadolivre_by_keyword(category, keyword)
    return jsonify(results)

@app.route('/search_buscape_by_category', methods=['GET'])
def get_buscape_products_by_category():
    category = request.args.get('category')
    results = search_buscape_by_category(category)
    return jsonify(results)

@app.route('/search_buscape_by_keyword', methods=['GET'])
def get_search_buscape_by_keyword():
    category = request.args.get('category')
    keyword = request.args.get('keyword')
    results = search_buscape_by_keyword(category, keyword)
    return jsonify(results)


@app.route('/searchall', methods=['GET'])
def search():
    category = request.args.get('category')
    keyword = request.args.get('keyword')
    results = search_all(category, keyword)
    return jsonify(results)


if __name__ == '__main__':
    app.run()