from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, request, render_template, url_for, abort, session
from admin.admin import app as app_admin
from author.author import app as app_author
from reader.reader import app as app_reader
from auth import bp


app_home = Flask(__name__)
app_home.secret_key = '123456'
app_home.register_blueprint(bp)


@app_home.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@app_home.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return render_template("demo.html")


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


