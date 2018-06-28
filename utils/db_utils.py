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
    return rows



def select_HX(mark,kind,search=None,page=None,st=None):
    if not page:
        page = 1;
    if mark == "all":
        if kind == "book":
            select_sql= Select(["id","book_name","author","catalog","current_state","recent_update_time","check_state"],staticTables=['Book']
                               ,limit=24*page)
            query = connection.sqlrepr(select_sql)
            print(query)
            rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

            return [json.dumps({'id': r[0], 'bookname':r[1],'author': r[2],'catalog':r[3], 'current_state': r[4],
                                'recent_update_time': r[5], 'check': r[6]})
                    for r in rows]
        elif kind == "author":
            select_sql = Select(
                ["id", "author_name", "author_pass", "description", "author_class","nick_name", "check_state"],
                staticTables=['Author']
                , limit=12 * page)
            query = connection.sqlrepr(select_sql)
            print(query)
            rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

            return [json.dumps({'id': r[0], 'authorname': r[1], 'authorpass': r[2], 'description': r[3], 'author_class': r[4],
                                'nick_name': r[5], 'check': r[6]})
                    for r in rows]
        elif kind == "reader":
            select_sql = Select(
                ["id", "reader_name", "reader_pass"],
                staticTables=['Reader']
                , limit=12 * page)
            query = connection.sqlrepr(select_sql)
            print(query)
            rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

            return [json.dumps(
                {'id': r[0], 'reader_name': r[1], 'reader_pass': r[2]})
                    for r in rows]
    else:
        if kind =="book":
            if search == "id":
                select_sql = Select(
                    ["id", "book_name", "author", "catalog", "current_state", "recent_update_time", "check_state"],
                    staticTables=['Book']
                    ,where="id = '%d'" % (st))
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [json.dumps({'id': r[0], 'bookname': r[1], 'author': r[2], 'catalog': r[3], 'current_state': r[4],
                                    'recent_update_time': r[5], 'check': r[6]})
                        for r in rows]
            elif search == "book":
                select_sql = Select(
                    ["id", "book_name", "author", "catalog", "current_state", "recent_update_time", "check_state"],
                    staticTables=['Book']
                    , where="book_name like '%s%s%s'" % ('%',st,'%'))
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [
                    json.dumps({'id': r[0], 'bookname': r[1], 'author': r[2], 'catalog': r[3], 'current_state': r[4],
                                'recent_update_time': r[5], 'check': r[6]})
                    for r in rows]
            elif search == "author":
                select_sql = Select(
                    ["id", "book_name", "author", "catalog", "current_state", "recent_update_time", "check_state"],
                    staticTables=['Book']
                    , where="author like '%s%s%s'" % ('%',st,'%'))
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [
                    json.dumps({'id': r[0], 'bookname': r[1], 'author': r[2], 'catalog': r[3], 'current_state': r[4],
                                'recent_update_time': r[5], 'check': r[6]})
                    for r in rows]
        elif kind =="author":
            if search == "id":
                select_sql = Select(
                    ["id", "author_name", "author_pass", "description", "author_class", "nick_name", "check_state"],
                    staticTables=['Author'],where="id = '%d'" % (st)
                    , limit=12 * page)
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [json.dumps(
                    {'id': r[0], 'authorname': r[1], 'authorpass': r[2], 'description': r[3], 'author_class': r[4],
                     'nick_name': r[5], 'check': r[6]})
                        for r in rows]
            elif search == "author_name":
                select_sql = Select(
                    ["id", "author_name", "author_pass", "description", "author_class", "nick_name", "check_state"],
                    staticTables=['Author'], where="author_name like '%s%s%s'" % ('%',st,'%')
                    , limit=12 * page)
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [json.dumps(
                    {'id': r[0], 'authorname': r[1], 'authorpass': r[2], 'description': r[3], 'author_class': r[4],
                     'nick_name': r[5], 'check': r[6]})
                    for r in rows]
        elif kind == "reader":
            if search == "id":
                select_sql = Select(
                    ["id", "reader_name", "reader_pass"],
                    staticTables=['Reader'], where="id = '%d'" % (st)
                    , limit=12 * page)
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [json.dumps(
                    {'id': r[0], 'readername': r[1], 'readerpass': r[2]})
                    for r in rows]
            elif search == "name":
                select_sql = Select(
                    ["id", "reader_name", "reader_pass"],
                    staticTables=['Reader'], where="reader_name like '%s%s%s'" % ('%',st,'%')
                    , limit=12 * page)
                query = connection.sqlrepr(select_sql)
                print(query)
                rows = connection.queryAll(query)[(page - 1) * 12: page * 12]

                return [json.dumps(
                    {'id': r[0], 'readername': r[1], 'readerpass': r[2]})
                    for r in rows]







def delete_HX(mark,id=None):
        Book.delete(id)




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
