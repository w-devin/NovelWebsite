#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:17
# @Author: Binyou
# @Site:
# @File: auth.py

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from utils.regist_utils import valid_author_regist
from utils.login_utils import valid_author_login
from utils.db_utils import Admin, Author, Reader,create_book, show_books



bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.author is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    author_id = session.get('author_id')

    if author_id is None:
        g.author = None
    else:
        g.author = Author.get(author_id)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not valid_author_regist(username, password):
            error = 'Author {} is already registered.'.format(username)
        else:
            return redirect(url_for('auth.login'))
        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        if not valid_author_login(username, password):
            error = 'Incorrect username or password.'
        print(error)
        if error is None:
            author = Author.selectBy(authorPass=password, authorName=username)[0]
            g.author = author
            session.clear()
            rows = show_books(author.id)
            session['author_id'] = author.id
            session['author_name'] = author.authorName
            session['main_book'] = show_books(author.id)
            session['number'] = len(show_books(author.id))
            return render_template('index.html',books = rows)
        flash(error)
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


