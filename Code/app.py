from flask import Flask, render_template, request, redirect, url_for
from histogram import histogram_dict, read_file
from markov_chain import higher_order, higher_order_walk, new_chain, create_sentence, order_sample, cleanup_text_file
import random

app = Flask(__name__)

@app.route('/')
def show_phrase():
    words = cleanup_text_file('txt_files/houseofquiet.txt')
    word_list = words.split()
    sentence = higher_order_walk(word_list, 40)

    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
