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


book_num = Book.select().count()
author_num = Author.select().count()
admin_num = Admin.select().count()
reader_num = Reader.select().count()


def select_HX(mark,page=None):
    if not page:
        page = 1;
    if mark == "book":
        select_sql= Select(["id","book_name","author","catalog","current_state","recent_update_time","check_state"],staticTables=['Book'],
                           orderBy="heat", limit=12)
        query = connection.sqlrepr(select_sql)
        rows = connection.queryAll(query)[(page - 1) * 12: page * 12]
        print(rows)
        return [json.dumps({'id': r[0], 'bookname':r[1],'author': r[2],'catalog':r[3], 'current_state': r[4],
                            'recent_update_time': r[5], 'check': r[6]})
                for r in rows]


def select_book_byclass(class_, page=None):
    if page is None:
        page = 1
    if class_ in list(range(9)):
        if class_ != 8:
            catalog = ["科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道"]
            select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                            where="catalog = '%s'" % (catalog[class_]), orderBy="heat", limit=12, start=(page-1)*12)
        else:
            select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'], orderBy="heat")
        query = connection.sqlrepr(select_sql)
        rows = connection.queryAll(query)
    return [{'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]}
        for r in rows]


def select_book(mark, catagory=None , page=None):
    if not page:
        page = 1
    if mark == "all":
        return [json.dumps({'name': b.bookName, 'author': b.author, 'description': b.bookDescription, 'link': b.link, 'cover': b.cover}) for b in Book.select(orderBy='heat')[(page-1)*12: page*12]]
    elif mark == "finished":
        select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                            where="current_state = '%s'" % ('完成'), orderBy="heat", limit=12, start=(page-1)*12)
        query = connection.sqlrepr(select_sql)
        rows = connection.queryAll(query)
        return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                for r in rows]
    else:
        if mark == "order":
            if catagory in list(range(1, 9)):
                catalog = ["科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道"]
                select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                                    where="catalog = '%s'" % (catalog[catagory]), orderBy="heat", limit=12, start=(page-1)*12)
                query = connection.sqlrepr(select_sql)
                rows = connection.queryAll(query)
                return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                        for r in rows]
            return None
        return None


def search_book(keyword):
    select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                        where="book_name like '%s%s%s'" % ('%', keyword, '%'))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    return [{'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]}
        for r in rows]
