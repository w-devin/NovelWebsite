#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:58
# @Author: Binyou
# @Site: 
# @File: reader.py

from flask import Flask, request, render_template
from utils.login_utils import valid_reader_login

app = Flask(__name__)


@app.route('/<reader_name>')
def index(reader_name):
    return render_template('index.html', reader=reader_name)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_reader_login(request.form['username'], request.form['password']):
            return render_template('index.html', reader=request.form['username'])
        else:
            error = 'Invalid username/password!'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()

