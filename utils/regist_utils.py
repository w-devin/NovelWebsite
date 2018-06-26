#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:23
# @Author: Binyou
# @Site: 
# @File: regist_utils.py

from sqlobject import *
from sqlobject.sqlbuilder import *

connection_str = "mysql://root:root@123.206.84.237:3306/EBook?driver=connector"
connection = connectionForURI(connection_str)
sqlhub.processConnection = connection


# 注册管理员
def valid_admin_login(username, password):
    select_sql = Select(["admin_name", "admin_pass"], staticTables=['Admin'], where="admin_name like '%s'" %(username))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return True
    return False


# 注册作者
def valid_author_regist(username, password):
    print(username,password)
    select_sql = Select(["author_name", "author_pass"], staticTables=['Author'], where="author_name = '%s'" %(username))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return False
    insert_sql = Insert('Author',values={'author_name':username,'author_pass':password})
    query = connection.sqlrepr(insert_sql)
    connection.query(query)
    return True


# 注册读者
def valid_reader_regist(username, password):
    print(username, password)
    select_sql = Select(["reader_name", "reader_pass"], staticTables=['Reader'], where="reader_name = '%s'" %(username))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    if rows:
        return False
    insert_sql = Insert('Reader', values={'reader_name': username, 'reader_pass': password})
    query = connection.sqlrepr(insert_sql)
    connection.query(query)
    return True