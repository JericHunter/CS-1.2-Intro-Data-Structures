from flask import Flask, render_template, request, redirect, url_for
from histogram import histogram_dict, read_file
from markov_chain import higher_order, higher_order_walk, new_chain, create_sentence, order_sample, cleanup_text_file
import random
from pymongo import MongoClient
import os

import tweepy

# Set up flask app
app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetgen')
client = MongoClient(host=f'{host}?authSource=admin')
db = client.get_default_database()

app_key = 'rCguhoSNkQGrj2WfowC0iI4rj'
app_secret = 'nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ'
access_token = '992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX'
access_token_secret= 'tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G'


auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route('/')
def show_phrase():
    words = cleanup_text_file('txt_files/houseofquiet.txt')
    word_list = words.split()
    sentence = higher_order_walk(word_list, 40)

    return render_template('index.html', sentence=sentence)


@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    if request.method == 'POST':

        sentence = request.form.get('sentence')
        if len(sentence) > 280:
            return 'Length of sentence is longer than allowed tweet limit.'

        api.update_status(sentence)

        return 'Tweet was successful!'
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
