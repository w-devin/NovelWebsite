#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:17
# @Author: Binyou
# @Site:
# @File: auth.py

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify
)
from utils.login_utils import valid_admin_login
from utils.db_utils import Admin, Author, Reader
from admin.db_HX import select_HX,delete_HX,update_HX


bp = Blueprint('author', __name__, url_prefix='/author')


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


@bp.route('/author')
def author():
    return render_template('author_manager.html')


@bp.route('/author/select/author/<int:page>',methods=['GET'])
def select_author(page):
    print(page)
    res=select_HX("all","author",page=page)
    return jsonify({"res": res})


@bp.route('/delete',methods=['GET','POST'])
def delete_author():
    if request.method == 'POST':
        _id=request.form['id']
        print(_id)
        delete_HX("author",_id)
    return "Success"


@bp.route('/select/author/id/<int:id>',methods=['GET'])
def select_someid_author(id):
    print(id)
    page=1;
    res=select_HX("some","author","id",page,id)
    return jsonify({"res": res})


@bp.route('/select/author/author/<mark>',methods=['GET'])
def select_someauthor_author(mark):
    print(mark)
    page=1;
    res=select_HX("some","author","author_name",page,mark)
    return jsonify({"res": res})


@bp.route('/update',methods=['POST'])
def bookupadte():
    if request.method == 'POST':
        _id = int(request.form['id'])
        print(_id)

        message = [request.form['authorpass'],request.form['authorclass'],request.form['new_check']]

        update_HX("author",_id,message)
    return "Success"
