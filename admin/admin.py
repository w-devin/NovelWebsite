#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:54
# @Author: Binyou
# @Site: 
# @File: admin.py

from flask import Flask, render_template, request, session, url_for, redirect
from utils.login_utils import valid_admin_login
from admin.auth import bp as auth_bp
from admin.book import bp as book_bp
from admin.author import bp as author_bp
from admin.reader import bp as reader_bp
from admin.check import bp as check_bp
from utils.db_utils import select_HX

app = Flask(__name__)
app.secret_key = '123456'
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(author_bp)
app.register_blueprint(reader_bp)
app.register_blueprint(check_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def home():
    if session.get('admin_id') is None:
        return redirect(url_for('auth.login'))
    return render_template('index.html')


@app.route('/select/<mark>')
def book(mark):
    res=select_HX(mark)
    return jsonify({"res": res})



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
