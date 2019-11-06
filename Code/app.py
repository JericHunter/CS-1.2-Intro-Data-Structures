from flask import Flask, render_template, request, redirect, url_for
from sample import sentences
from histogram import histogram_dict

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'txt_files/testing.txt'
    histogram = histogram_dict(text)
    sentence = sentences(histogram, 15)
    return render_template('base.html', tweet=sentence)
