#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-20 16:39
# @Author: Binyou
# @Site: 
# @File: login_utils.py

from sqlobject import *
from sqlobject.sqlbuilder import *

connection_str = "mysql://root:root@123.206.84.237:3306/EBook?driver=connector"
connection = connectionForURI(connection_str)
sqlhub.processConnection = connection


# 对管理员进行身份验证
def valid_admin_login(username, password):
    select_sql = Select(["admin_name", "admin_pass"], staticTables=['Admin'], where="admin_name like '%s' and admin_pass like '%s'" %(username, password))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return True
    return False


# 对作者身份进行身份验证
def valid_author_login(username, password):
    select_sql = Select(["author_name", "author_pass"], staticTables=['Author'], where="author_name = '%s' and author_pass = '%s'" %(username, password))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return True
    return False


# 对读者身份进行身份验证
def valid_reader_login(username, password):
    select_sql = Select(["reader_name", "reader_pass"], staticTables=['Reader'], where="reader_name = '%s' and reader_pass = '%s'" %(username, password))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return True
    return False
