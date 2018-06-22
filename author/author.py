#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:58
# @Author: Binyou
# @Site: 
# @File: author.py

from flask import Flask, render_template, request
from utils.login_utils import valid_author_login

app = Flask(__name__)


@app.route('/<author_name>')
def index(author_name):
    return render_template('index.html', author=author_name)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_author_login(request.form['username'], request.form['password']):
            return render_template('index.html', name=request.form['username'])
        else:
            error = 'Invalid username/password!'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()