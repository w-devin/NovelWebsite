from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import \
    ( Flask, request, render_template, url_for, session, jsonify)
from admin.admin import app as app_admin
from author.author import app as app_author
from auth import bp
from utils.db_utils import select_book


app_home = Flask(__name__)
app_home.secret_key = '123456'
app_home.register_blueprint(bp)
app_home.config['JSON_AS_ASCII'] = False


@app_home.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@app_home.route('/book/<mark>', methods=['GET'])
def book(mark):
    res = select_book(mark)
    return jsonify({"res": res})


@app_home.route('/book/order/<int:catagory>', methods=['GET'])
def book_order(catagory):
    # ("科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道")
    res = select_book('order', catagory=catagory)
    return jsonify({"res": res})



with app_home.test_request_context():
    # print(url_for('static', filename='style.css'))
    pass


# 通过分发请求的方式将模块集成起来
app = DispatcherMiddleware(app_home,{
    '/admin': app_admin,
    '/author': app_author,
})


if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)


