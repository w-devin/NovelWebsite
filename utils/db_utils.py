#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:56
# @Author: Binyou
# @Site: 
# @File: db_utils.py

from sqlobject import *
from sqlobject.sqlbuilder import *
from flask import json

connection_str = "mysql://root:root@123.206.84.237:3306/EBook?driver=connector"
connection = connectionForURI(connection_str)
sqlhub.processConnection = connection


class Book(SQLObject):
    class sqlmeta:
        table = "Book"
        fromDatabase = True


class Author(SQLObject):
    class sqlmeta:
        table = "Author"
        fromDatabase = True


class Admin(SQLObject):
    class sqlmeta:
        table = "Admin"
        fromDatabase = True


class Reader(SQLObject):
    class sqlmeta:
        table = "Reader"
        fromDatabase = True


#def create_book():

def select_book(mark, page=None):
    if not page:
        page = 1
    if mark == "all":
        return [json.dumps({'name': b.bookName, 'author': b.author, 'description': b.bookDescription, 'link': b.link, 'cover': b.cover}) for b in Book.select(orderBy='heat')[(page-1)*12: page*12]]
    elif mark == "finished":
        select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                            where="current_state = '%s'" % ('完成'), orderBy="heat")
        query = connection.sqlrepr(select_sql)
        rows = connection.queryAll(query)[(page-1)*12: page*12]
        print(rows)
        return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                for r in rows]
    else:
        if mark in [range(1, 9)]:
            catalog = ("科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道")
            catalog_index = int(mark)
            select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                                where="catalog = '%s'" % (catalog(catalog_index)), orderBy="heat")
            query = connection.sqlrepr(select_sql)
            rows = connection.queryAll(query)[(page-1)*12: page*12]
            return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                    for r in rows]
