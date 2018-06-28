#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:58
# @Author: Binyou
# @Site: 
# @File: author.py

from flask import Flask, render_template, request,session, url_for, redirect
from author.auth import bp as auth_bp
from author.book import bp as book_bp
from utils.db_utils import show_books

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.secret_key = "123456"


@app.route('/', methods=['GET'])
def index():
    if session.get('author_id') is None:
        return redirect(url_for('auth.login'))
    if request.method == 'GET':
        rows = show_books(session.get('author_id'))
        return render_template('index.html',books = rows)


if __name__ == '__main__':
    app.run()