#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:17
# @Author: Wang Ya wen
# @Site: 
# @File: auth.py

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from utils.regist_utils import valid_reader_regist
from utils.login_utils import valid_reader_login
from utils.db_utils import Reader


bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth/login'))
        return view(**kwargs)
    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        print('in load logged')
        g.user = Reader.get(user_id)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not valid_reader_regist(username, password):
            error = 'User {} is already registered.'.format(username)
        else:
            return render_template('login.html')
        flash(error)

    return render_template('register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not valid_reader_login(username, password):
            error = 'Incorrect username or password.'

        if error is None:
            g.user = Reader.selectBy(readerPass=password, readerName=username)[0]
            session.clear()
            session['user_id'] = g.user.id
            return redirect('/')
        flash(error)

    return render_template('login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

'''
    
'''