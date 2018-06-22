#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:54
# @Author: Binyou
# @Site: 
# @File: admin.py

from flask import Flask, render_template, request
from utils.login_utils import valid_admin_login

app = Flask(__name__)


@app.route('/<admin_name>')
def index(admin_name):
    return render_template('index.html', admin=admin_name)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_admin_login(request.form['username'], request.form['password']):
            return render_template('index.html', admin=request.form['username'])
        else:
            error = 'Invalid username/password!'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
