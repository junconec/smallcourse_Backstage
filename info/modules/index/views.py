from flask import render_template

from . import index_blue

# ������ҳ·��
@index_blue.route('/')
def index():
    return render_template('frame.html')


# ��ҳչʾ·��
@index_blue.route('/index/')
def index_data():
    return render_template('frame.html')

