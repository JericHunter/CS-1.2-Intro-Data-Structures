from flask import Flask, render_template, request, redirect, url_for
from histogram import histogram_dict, read_file
from markov_chain import higher_order, higher_order_walk, new_chain, create_sentence, order_sample, cleanup_text_file
import random

import os
import twitter  # for tweeting

# Set up flask app
app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetgen')
client = MongoClient(host=f'{host}?authSource=admin')
db = client.get_default_database()

# Setup twitter API
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.getenv('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

twitter_api = twitter.Api(consumer_key='nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ',
                          consumer_secret='nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ',
                          access_token_key='992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX',
                          access_token_secret='tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G')

@app.route('/')
def show_phrase():
    words = cleanup_text_file('txt_files/houseofquiet.txt')
    word_list = words.split()
    sentence = higher_order_walk(word_list, 40)

    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
