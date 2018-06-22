#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-21 10:56
# @Author: Binyou
# @Site: 
# @File: db_utils.py

from sqlobject import *
from sqlobject.sqlbuilder import *

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