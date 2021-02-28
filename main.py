from flask import Flask, render_template, url_for, request, redirect
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from ebay_api_testing import result_array
from ebay_api_testing import result_cost
from ebay_api_testing import result_images
from ebay_api_testing import result_link


app = Flask(__name__)


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/ebaything')
def display_ebaything():
    c = result_array
    return render_template('ebaything.html', title=c, cost=result_cost, image=result_images, link=result_link)

