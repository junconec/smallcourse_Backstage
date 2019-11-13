# -*- coding:utf-8 -*-
import time

from flask import render_template, request, jsonify
from . import orderCenter_blue
import requests
from model.Order import Order
from info import conn,cur, conn3, cur3
from config import MYSQL_TB, MYSQL_DB_2, MYSQL_TB_2


# 订单中心首页
@orderCenter_blue.route('/')
def orderCenter():
    # 获取分页的信息
    # 获取要展示的页数
    if request.method == 'GET':
        p = int(request.args.get('p', 1))
    else:
        p = int(request.form.get('p', 1))

    # 获取每页展示的数量
    if request.method == 'GET':
        limit = int(request.args.get('limit', 20))
    else:
        limit = int(request.form.get('limit', 20))

    # # 获取总数
    total_count = Order.query.filter(Order.course_id == 76,Order.class_id == 121, Order.status == 2).count()

    # 获取分页数据
    pagination = Order.query.filter(Order.course_id == 76,Order.class_id == 121, Order.status == 2).order_by(Order.create_time.desc()).paginate(p, per_page=limit, error_out=False)
    order_list = pagination.items

    # 转换时间戳为时间
    time_list = []
    for order in order_list:
        timeStamp = order.create_time
        localTime = time.localtime(timeStamp)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        time_list.append(strTime)

    # 获取token
    body = {"grant_type": "password",
            "username": "15501036155",
            "password": "aa123456"}

    headers = {
        'Authorization': 'Basic MTAwMDAwMDA6OWUyMWNkZTMtNjRkZS00OTc2LWI4Y2MtMzI3NTQ2ZDJlZTIy'
    }
    token = requests.post('https://deal-api.kuick.cn/kuickuser/oauth2/access_token', headers=headers, data=body).json()['access_token']

    # 获取所有人的名字
    sql = 'SELECT DISTINCT (realname) FROM {}'.format(MYSQL_TB_2)
    cur3.execute(sql)
    name_list = []
    for name in cur3.fetchall():
        name_list.append(name[0])

    json_data = {}
    json_data['order_list'] = order_list
    json_data['time_list'] = time_list
    json_data['current_page'] = p
    json_data['total_count'] = total_count
    json_data['page_limit'] = limit
    json_data['xiaozhuan'] = ''
    json_data['name_list'] = name_list
    # json_data['class_list'] = class_list

    # 渲染到模板
    return render_template('orderCenter/orderCenter_index.html', json_data=json_data, token=token)


# 订单中心选中数据 导入入群操作
@orderCenter_blue.route('/insertChecked', methods=['GET', 'POST'])
def insertChecked():
    orderIds = request.form.get('orderIds')
    classId = request.form.get('classId')
    is_all_select = request.form.get('is_all_select')
    xiaozhuan = request.form.get('xiaozhuan')
    start_time = request.form.get('start_time')
    finish_time = request.form.get('finish_time')

    # 处理orderids
    orderIds = orderIds.split(',')

    if not classId:
        return jsonify(errno=1001, errmsg="请选择要导入的群")

    # # 判断是否选择全选  如果选择了全选 那么需要加上查询条件
    if is_all_select:
        # 先查询出所有的符合条件的order  再导入
        if start_time and finish_time:
            # 将其转换为时间数组
            timeStruct1 = time.strptime(start_time, "%Y-%m-%d")
            timeStruct2 = time.strptime(finish_time, "%Y-%m-%d")
            # 转换为时间戳:
            start_time = int(time.mktime(timeStruct1))
            finish_time = int(time.mktime(timeStruct2))
        elif start_time and not finish_time:
            timeStruct1 = time.strptime(start_time, "%Y-%m-%d")
            start_time = int(time.mktime(timeStruct1))
        elif not start_time and finish_time:
            timeStruct1 = time.strptime(finish_time, "%Y-%m-%d")
            finish_time = int(time.mktime(timeStruct1))
        else:
            pass

        sql = 'SELECT qr_code FROM sys_seller ss, sys_device_seller sds, sys_user_device sud, sys_user su WHERE' \
              ' su.realname="{xiaozhuan}" AND sud.user_id= su.id AND sds.device_id = sud.device_id AND ss.id' \
              ' = sds.seller_id'.format(
            xiaozhuan=xiaozhuan
        )
        cur3.execute(sql)
        rets = cur3.fetchall()
        qr_code_list = []
        for qr_code in rets:
            qr_code_list.append(qr_code[0])

        qr_code_tuple = tuple(qr_code_list)

        # 查询分为6中情况
        if all([xiaozhuan, start_time, finish_time]):
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple),
                                            Order.create_time.__ge__(start_time), Order.create_time.__le__(finish_time))
        elif xiaozhuan and not (start_time) and not (finish_time):
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple))
        elif not (xiaozhuan) and start_time and not (finish_time):
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__ge__(start_time))
        elif not (xiaozhuan) and not (start_time) and finish_time:
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__le__(finish_time))
        elif xiaozhuan and start_time and not (finish_time):
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple),
                                            Order.create_time.__ge__(start_time))
        elif xiaozhuan and not (start_time) and finish_time:
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple),
                                            Order.create_time.__le__(finish_time))
        elif not (xiaozhuan) and start_time and finish_time:
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__ge__(start_time), Order.create_time.__le__(finish_time))
        elif not (xiaozhuan) and not (start_time) and not (finish_time):
            filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2)


        orderIds = []
        order_rets = filter_ret.all()
        for order_el in order_rets:
            orderIds.append(order_el.unionid)

    # 如果没有全选 （正常逻辑） 和 全选处理过后
    for orderId in orderIds:
        # 把orderId跟群id建立一对多关系
        sql = 'INSERT INTO {} (class_id, member_id) values("{}", "{}")'.format(MYSQL_TB, classId, orderId)
        cur.execute(sql)
    conn.commit()

    return jsonify(errno=200, errmsg="导入成功")


# 订单中心 查询
@orderCenter_blue.route('/searchOrder')
def searchOrder():
    # 获取分页的信息
    # 获取要展示的页数
    if request.method == 'GET':
        p = int(request.args.get('p', 1))
        limit = int(request.args.get('limit', 20))
        xiaozhuan = request.args.get('xiaozhuan', '')
        start_time = request.args.get('start_time', '')
        finish_time = request.args.get('finish_time', '')
        token = request.args.get('token', '')

    else:
        p = int(request.form.get('p', 1))
        limit = int(request.form.get('limit', 20))
        xiaozhuan = request.form.get('xiaozhuan', '')
        start_time = request.form.get('start_time', '')
        finish_time = request.form.get('finish_time', '')
        token = request.args.get('token', '')

    start_time_old = start_time
    finish_time_old = finish_time

    # 处理两个时间参数 转化为时间戳
    if start_time and finish_time:
        # 将其转换为时间数组
        timeStruct1 = time.strptime(start_time, "%Y-%m-%d")
        timeStruct2 = time.strptime(finish_time, "%Y-%m-%d")
        # 转换为时间戳:
        start_time = int(time.mktime(timeStruct1))
        finish_time = int(time.mktime(timeStruct2))
    elif start_time and not finish_time:
        timeStruct1 = time.strptime(start_time, "%Y-%m-%d")
        start_time = int(time.mktime(timeStruct1))
    elif not start_time and finish_time:
        timeStruct1 = time.strptime(finish_time, "%Y-%m-%d")
        finish_time = int(time.mktime(timeStruct1))
    else:
        pass

    sql = 'SELECT qr_code FROM sys_seller ss, sys_device_seller sds, sys_user_device sud, sys_user su WHERE' \
          ' su.realname="{xiaozhuan}" AND sud.user_id= su.id AND sds.device_id = sud.device_id AND ss.id' \
          ' = sds.seller_id'.format(
            xiaozhuan=xiaozhuan
            )
    cur3.execute(sql)
    rets = cur3.fetchall()
    qr_code_list = []
    for qr_code in rets:
        qr_code_list.append(qr_code[0])

    qr_code_tuple = tuple(qr_code_list)


    # 查询分为6中情况
    if all([xiaozhuan, start_time, finish_time]):
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple), Order.create_time.__ge__(start_time), Order.create_time.__le__(finish_time))
    elif xiaozhuan and not(start_time) and not(finish_time):
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple))
    elif not(xiaozhuan) and start_time and not(finish_time):
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__ge__(start_time))
    elif not(xiaozhuan) and not(start_time) and finish_time:
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__le__(finish_time))
    elif xiaozhuan and start_time and not(finish_time):
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple), Order.create_time.__ge__(start_time))
    elif xiaozhuan and not(start_time) and finish_time:
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.qr_code.in_(qr_code_tuple), Order.create_time.__le__(finish_time))
    elif not(xiaozhuan) and start_time and finish_time:
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2, Order.create_time.__ge__(start_time), Order.create_time.__le__(finish_time))
    elif not(xiaozhuan) and not(start_time) and not(finish_time):
        filter_ret = Order.query.filter(Order.course_id == 76, Order.class_id == 121, Order.status == 2)

    # # 获取总数
    total_count = filter_ret.count()

    # 获取分页数据
    pagination = filter_ret.order_by(Order.create_time.desc()).paginate(p, per_page=limit, error_out=False)
    order_list = pagination.items

    # 转换时间戳为时间
    time_list = []
    for order in order_list:
        timeStamp = order.create_time
        localTime = time.localtime(timeStamp)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        time_list.append(strTime)

    # 获取所有人的名字
    sql = 'SELECT DISTINCT (realname) FROM {}'.format(MYSQL_TB_2)
    cur3.execute(sql)
    name_list = []
    for name in cur3.fetchall():
        name_list.append(name[0])

    json_data = {}
    json_data['order_list'] = order_list
    json_data['time_list'] = time_list
    json_data['current_page'] = p
    json_data['total_count'] = total_count
    json_data['page_limit'] = limit
    json_data['xiaozhuan'] = xiaozhuan
    json_data['start_time'] = start_time_old
    json_data['finish_time'] = finish_time_old
    json_data['name_list'] = name_list
    # json_data['class_list'] = class_list

    # 渲染到模板
    return render_template('orderCenter/orderCenter_index.html', json_data=json_data, token=token)