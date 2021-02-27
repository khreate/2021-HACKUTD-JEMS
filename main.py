from flask import Flask, render_template, url_for, request, redirect
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from ebay_api_testing import result_array


app = Flask(__name__)


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/ebaything')
def display_ebaything():
    c = result_array
    return render_template('ebaything.html', array=c)
