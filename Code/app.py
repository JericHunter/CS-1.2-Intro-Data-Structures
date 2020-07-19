from flask import Flask, render_template, request, redirect, url_for
from histogram import histogram_dict, read_file
from markov_chain import higher_order, higher_order_walk, new_chain, create_sentence, order_sample, cleanup_text_file
import random
from pymongo import MongoClient
import os
import sys
import json
import tweepy

# Set up flask app
app = Flask(__name__)



# funciton that just updates twitter status 'tweet'
consumer_key = ('rCguhoSNkQGrj2WfowC0iI4rj')        # consumer key
consumer_secret = ('nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ')       # consumer secret
access_token = ('992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX')            # access token
token_secret = ('tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G')          # token secret
# Oauth Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)
# authenticate
api = tweepy.API(auth)
words = cleanup_text_file('txt_files/houseofquiet.txt')
word_list = words.split()
sentence = higher_order_walk(word_list, 40)

@app.route('/', methods=['GET', 'POST'])
def show_phrase():
    # words = cleanup_text_file('txt_files/houseofquiet.txt')
    # word_list = words.split()
    sentence = higher_order_walk(word_list, 40)

    return render_template('index.html', sentence=sentence)


# app_key = 'rCguhoSNkQGrj2WfowC0iI4rj'
# app_secret = 'nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ'
# access_token = '992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX'
# access_token_secret= 'tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G'
#
#
# auth = tweepy.OAuthHandler(app_key, app_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)


@app.route('/tweet', methods=['POST'])
def tweet():
    if request.method == 'POST':

        # sentence = request.form.get(sentence)
        # if len(sentence) > 280:
        #     return 'Length of sentence is longer than allowed tweet limit.'

        api.update_status(status=sentence)

        return 'Tweet was successful!'
if __name__ == "__main__":
    app.run(debug=True)
