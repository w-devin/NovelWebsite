from sqlobject import *
from sqlobject.sqlbuilder import *
from flask import json
from utils.db_utils import *



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


def update_HX(mark,id,message):
    if mark =="book":
        update_sql = Update('Book',
                            values={'catalog': message[0], 'current_state': message[1], 'check_state': message[2]}, where="id = %d" % (id))

        query = connection.sqlrepr(update_sql)
        print(query)
        connection.query(query)
    elif mark == "author":
        update_sql = Update('Author',
                            values={'author_pass': message[0], 'author_class': message[1], 'check_state': message[2]},
                            where="id = %d" % (id))
        query = connection.sqlrepr(update_sql)
        print(query)
        connection.query(query)
    else:
        update_sql = Update('Reader',
                            values={'reader_pass': message[0]},
                            where="id = %d" % (id))
        query = connection.sqlrepr(update_sql)
        connection.query(query)

