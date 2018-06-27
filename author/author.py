#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:58
# @Author: Binyou
# @Site: 
# @File: author.py

from flask import Flask, render_template, request,session, url_for, redirect
from author.auth import bp

app = Flask(__name__)
app.register_blueprint(bp)
app.secret_key = "123456"


@app.route('/', methods=['GET'])
def index():
    if session.get('author_id') is None:
        return redirect(url_for('auth.login'))
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()