from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import \
    ( Flask, request, render_template, url_for, session, abort, jsonify, redirect)
from admin.admin import app as app_admin
from author.author import app as app_author
from reader.reader import app as app_reader
from auth import bp
from book_chapter_spider import get_chapter, get_chapter_content
from utils.db_utils import select_book, search_book, select_book_byclass
from utils.book_utils import get_chapter_list
from utils.db_utils import Book


app_home = Flask(__name__)
app_home.secret_key = '123456'
app_home.register_blueprint(bp)
app_home.config['JSON_AS_ASCII'] = False


@app_home.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@app_home.route('/book/<mark>/<int:page>', methods=['GET'])
def book(mark, page):
    res = select_book(mark, page=page)
    return jsonify({"res": res})


@app_home.route('/book/order/<int:catagory>', methods=['GET'])
def book_order(catagory):
    # ("科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道")
    res = select_book('order', catagory=catagory)
    return jsonify({"res": res})


@app_home.route('/book/catagory/<int:catagory>/<int:page>', methods=['GET'])
def book_class(catagory, page):
    res = select_book_byclass(class_=catagory, page=page)
    return jsonify({"res": res})


@app_home.route('/read/book/<book_num>/<chapter>', methods=['GET'])
def chapter_page(book_num, chapter):
    if request.method == 'GET':
        url = "https://m.qu.la/book/%s/%s.html" %(book_num, chapter)
        content, title = get_chapter_content(url)
        return render_template('chapter.html', last="/read/book/%s/%d" % (book_num, int(chapter)-1), return_="/read/book/%s" % book_num, next="/read/book/%s/%d" % (book_num, int(chapter)+1), content=content, title = title)


@app_home.route('/read/book/<book_num>/', methods=['GET'])
def book_page(book_num):
    if request.method == 'GET':
        url = "https://m.qu.la/booklist/%s.html" %book_num
        book = Book.selectBy(link='/book/%s/' %book_num)[0]
        path = get_chapter(url)
        chapters = get_chapter_list(path)
        return render_template('book.html', chapters = chapters,  book=book)




@app_home.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if keyword:
        rows = search_book(keyword)
        return render_template('search.html', books=rows)
    return render_template("index.html")


with app_home.test_request_context():
    # print(url_for('static', filename='style.css'))
    pass


# 通过分发请求的方式将模块集成起来
app = DispatcherMiddleware(app_home,{
    '/admin': app_admin,
    '/author': app_author,
    '/reader': app_reader,
})


if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)


