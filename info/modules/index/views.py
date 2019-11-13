from flask import render_template

from . import index_blue

# 访问主页路由
@index_blue.route('/')
def index():
    return render_template('frame.html')


# 主页展示路由
@index_blue.route('/index/')
def index_data():
    return render_template('frame.html')

