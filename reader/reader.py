#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 20:54
# @Author: Wang Ya wen
# @Site: 
# @File: reader.py

from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = '234567'


@app.route('/')
def home():
    user_id = session.get('user_id')
    if user_id is None:
        return render_template('login.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
