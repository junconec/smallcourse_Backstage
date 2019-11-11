# -*- coding:utf-8 -*-
import requests
from flask import render_template, request
from . import createQun_blue

from model.Order import Order


# 建群管理首页
@createQun_blue.route('/')
def index():
    body = {"grant_type": "password",
            "username": "15501036155",
            "password": "aa123456"}

    headers = {
        'Authorization': 'Basic MTAwMDAwMDA6OWUyMWNkZTMtNjRkZS00OTc2LWI4Y2MtMzI3NTQ2ZDJlZTIy'
    }
    token = requests.post('https://deal-api.kuick.cn/kuickuser/oauth2/access_token', headers=headers, data=body).json()['access_token']

    # # 渲染到模板
    return render_template('createQun/create_qun.html', token=token)


# 建群管理建群 --
@createQun_blue.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        kuick_id = request.args.get('kuick_id', '')
        qun_img = request.args.get('qun_img', '')
        qishu = request.args.get('qishu', '')
        qunhao = request.args.get('qunhao', '')
        shequn = request.args.get('shequn', '')
        start_class_time = request.args.get('start_class_time', '')
        token = request.args.get('token', '')
    else:
        kuick_id = request.form.get('kuick_id', '')
        qun_img = request.form.get('qun_img', '')
        qishu = request.form.get('qishu', '')
        qunhao = request.form.get('qunhao', '')
        shequn = request.form.get('shequn', '')
        start_class_time = request.form.get('start_class_time', '')
        token = request.form.get('token', '')

    beizhu = qishu + '\n' + shequn + '\n' + start_class_time
    qun_name = qunhao+'群'

    # 获取到几个参数后   获取新的token  并且得到建群 接口
    create_qun_url = 'https://deal-admin.kuick.cn/api/v1.7/app/e5b1ace0-f756-4327-94a7-053eb890d327/' \
                     'customer-swarms?access_token={}'.format(token)
    body_2 = {
        'kuick_user_id': kuick_id,
        'name': qun_name,
        'photo_url': qun_img,
        'comment': beizhu
    }

    # 建群请求
    status = requests.post(create_qun_url, data=body_2).json()['status']

    if status == 1:
        return render_template('createQun/create_qun.html', token=token)

    # # 渲染到模板
    return render_template('createQun/create_qun.html', token=token)

