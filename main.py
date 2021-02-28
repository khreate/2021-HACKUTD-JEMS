from flask import Flask, render_template, url_for, request, redirect
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from ebay_api_testing import *


app = Flask(__name__)

keyword = ' '


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/ebaysearch', methods=["POST", "GET"])
def get_search_query():
    keyword = request.data.decode('utf-8')
    return keyword


@app.route('/ebaything', methods=["POST", "GET"])
def display_ebaything():
    get_search_query()
    print(request.data)
    c = ebay_title(keyword)
    cost = ebay_cost(keyword)
    image = ebay_image(keyword)
    link = ebay_link(keyword)

    return render_template('ebaything.html', title=c, cost=cost, image=image, link=link)


@app.route('/budget')
def display_budget():
    return render_template('budget.html')
