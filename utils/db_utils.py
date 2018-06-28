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


def create_book(ins):
    if ins is None:
        return False
    else:
        insert_sql = Insert('Book', values={'book_name': ins[0], 'book_description': ins[1],
                                               'catalog': ins[2], 'author': ins[3], 'link':ins[4],'author_id':ins[5]})
        query = connection.sqlrepr(insert_sql)
        connection.query(query)
        return True

def update_link(link,id):
    update_sql = Update('Book',values={'link':link,'current_state':'连载'},where='id=%d'%(id))
    query = connection.sqlrepr(update_sql)
    connection.query(query)

def update_bookmes(id,message):
    update_sql = Update('Book',values={'book_name':message[0],'book_description':message[1],'catalog':message[2],'current_state':message[3]},where='id=%d'%(id))
    query = connection.sqlrepr(update_sql)
    connection.query(query)

def show_books(authorid):
    select_sql = Select(["id", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                        where="author_id = '%d'" % (authorid))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    return rows

def author_select_book(bookid):
    select_sql = Select(["book_name", "book_description", "catalog", "current_state","id"], staticTables=['Book'],
                        where="id = '%d'" % (bookid))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    print(rows)
    return rows

def select_book(mark, catagory=None , page=None):
    if not page:
        page = 1
    if mark == "all":
        return [json.dumps({'name': b.bookName, 'author': b.author, 'description': b.bookDescription, 'link': b.link, 'cover': b.cover}) for b in Book.select(orderBy='heat')[(page-1)*12: page*12]]
    elif mark == "finished":
        select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                            where="current_state = '%s'" % ('完成'), orderBy="heat", )
        query = connection.sqlrepr(select_sql)
        rows = connection.queryAll(query)[(page-1)*12: page*12]
        return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                for r in rows]
    else:
        if mark == "order":
            if catagory in list(range(1, 9)):
                catalog = ["科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道"]
                select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                                    where="catalog = '%s'" % (catalog[catagory]), orderBy="heat")
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page-1)*12: page*12]
                return [json.dumps({'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]})
                        for r in rows]


def search_book(keyword):
    select_sql = Select(["author", "book_name", "book_description", "link", "cover"], staticTables=['Book'],
                        where="book_name like '%s%s%s'" % ('%', keyword, '%'))
    query = connection.sqlrepr(select_sql)
    rows = connection.queryAll(query)
    return [{'name': r[1], 'author': r[0], 'description': r[2], 'link': r[3], 'cover': r[4]}
        for r in rows]
