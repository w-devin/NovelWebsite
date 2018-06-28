import functools
import requests
import os
from bs4 import BeautifulSoup

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from utils.db_utils import Admin, Author, Reader,create_book,Book,update_link,show_books,author_select_book,update_bookmes,select_link

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/updatebook', methods=('GET', 'POST'))
def updatebook():
    if request.method == 'POST':
        row = author_select_book(int(request.form['bookid']))[0]
        return render_template("book/Personal.html", book=row)


@bp.route('/updatebookbyid', methods=('GET', 'POST'))
def updatebookbyid():
    if request.method == 'POST':
        message = [request.form['bookname'],request.form['bookdescription'],request.form['catalog'],request.form['currentstate']]
        update_bookmes(int(request.form['bookid']),message)
        return jsonify({"code":200, "result": '修改成功'})

@bp.route('/addchapter', methods=('GET', 'POST'))
def addchapter():
    if request.method == 'POST':
        bookid = int(request.form['bookid'])
        return render_template('book/chapter.html',bookid = bookid)

@bp.route('/addChapter', methods=('GET', 'POST'))
def addChapter():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['text']
        row = select_link(int(request.form['bookid']))[0]
        link = row[-1]
        print(link)
        if os.path.exists('static%s.txt' % link):
            with open('static%s.txt' % link, 'r', encoding='utf8') as f:
                length = len(f.readlines()) + 1
            with open('static%s.txt' % link, 'a', encoding='utf8') as f:
                f.write(",".join(["%s/%s.html" % (link, length), '第%s章 %s' % (length, title)]) + '\n')
            with open('static/chapter/%s.html' % length, 'a', encoding='utf8') as f:
                f.write(",".join(["%s" % title + '\n' + '%s' % content]))
        if not os.path.exists('static%s.txt' % link):
            with open('static%s.txt' % link, 'w', encoding='utf8') as f:
                    f.write(",".join(["%s/1.html" % link, '第1章 %s' % title ])+'\n')
            with open('static/chapter/1.html', 'w', encoding='utf8') as f:
                f.write(",".join(["%s" % title+'\n'+ '%s' % content]))

        return jsonify({"code": 200, "result": '添加成功'})


@bp.route('/createbook', methods=('GET', 'POST'))
def createbook():
    if request.method == 'GET':
        return render_template('auth/createbook.html')
    if request.method == 'POST':
        ins = [request.form['bookname'], request.form['bookdescription'], request.form['catalog'], session.get('author_name'),"link",session.get('author_id')]
        books = Book.selectBy(bookName = request.form['bookname'])
        while books.count() == 0:
            if not create_book(ins):
                error = 'incomplete information'
            else:
                book = Book.selectBy(bookName=request.form['bookname'], author=session.get('author_name'))[0]
                link = '/book/' + str(book.id)
                update_link(link, book.id)
                return jsonify({"code": 200, "result": '添加成功'})
            flash(error)
        error = 'bookname is repeat'
        return redirect(url_for('book.createbook'))



