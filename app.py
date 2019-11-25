from flask import Flask, render_template, request, redirect, url_for
import os
from sample import sampling, word_probability, get_count, sentence
from histogram import histogram_dict, read_file
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

client = MongoClient(host=host)
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


app = Flask(__name__)


@app.route('/')
def index():
    text_file = read_file('txt_files/testing.txt')
    histogram = histogram_dict(text_file)
    count = get_count(histogram_dict(text_file))
    total = len(text_file)

    # ' '.join(sentence(count, total, histogram))
    rand_sentence = sentence(count, total, histogram)
    return render_template('index.html', rand_sentence=rand_sentence)


if __name__ == '__main__':
    app.run(debug=True)
