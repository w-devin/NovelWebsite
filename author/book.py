import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from utils.db_utils import Admin, Author, Reader,create_book,Book,update_link,show_books,author_select_book,update_bookmes

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/updatebook', methods=('GET', 'POST'))
def updatebook():
    if request.method == 'POST':
        rows = author_select_book(int(session.get('main_book')))[0][1]
        return render_template('book/update.html',book = rows)

@bp.route('/updatebookbyid', methods=('GET', 'POST'))
def updatebookbyid():
    if request.method == 'POST':
        message = [request.form['bookname'],request.form['bookdescription'],request.form['catalog'],request.form['currentstate']]
        update_bookmes(int(request.form['bookid']),message)
        rows = show_books(session.get('author_id'))
        return render_template("index.html", books=rows)

@bp.route('/addchapter', methods=('GET', 'POST'))
def addchapter():
    if request.method == 'POST':
        return render_template('book/chapter.html')

@bp.route('/addChapter', methods=('GET', 'POST'))
def addChapter():
    if request.method == 'POST':
        id = int(request.form['bookid'])
        print(request.form['title'])
        print(request.form['text'])
        return render_template('book/chapter.html')


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
                link = '/book/' + str(book.id) + '/'
                update_link(link, book.id)
                rows = show_books(session.get('author_id'))
                return render_template("index.html", books=rows)
            flash(error)
        error = 'bookname is repeat'
        return redirect(url_for('book.createbook'))



