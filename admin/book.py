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
from utils.login_utils import valid_admin_login
from utils.db_utils import Admin, Author, Reader


bp = Blueprint('book', __name__, url_prefix='/book')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.admin is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.before_app_request
def load_logged_in_admin():
    admin_id = session.get('admin_id')

    if admin_id is None:
        g.admin = None
    else:
        g.admin = Admin.get(admin_id)


@bp.route('/book')
def book():
    return render_template('book_manager.html')


