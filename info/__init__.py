# -*- coding: UTF-8 -*-
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PW, MYSQL_DB, MYSQL_TB,MYSQL_HOST_2,MYSQL_PORT_2, MYSQL_USER_2, MYSQL_PW_2, MYSQL_DB_1, MYSQL_DB_2

app = Flask(__name__)

# 配置
app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)


# 创建本地数据库对象
conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PW, db=MYSQL_DB, charset='utf8')
cur = conn.cursor()

# 创建云数据库对象
# conn2 = pymysql.connect(host=MYSQL_HOST_2, port=MYSQL_PORT_2, user=MYSQL_USER_2, passwd=MYSQL_PW_2, db=MYSQL_DB_1, charset='utf8')
# cur2 = conn2.cursor()

# 创建云数据库对象
conn3 = pymysql.connect(host=MYSQL_HOST_2, port=MYSQL_PORT_2, user=MYSQL_USER_2, passwd=MYSQL_PW_2, db=MYSQL_DB_2, charset='utf8')
cur3 = conn3.cursor()



# 注册主页蓝图
from info.modules.index import index_blue
app.register_blueprint(index_blue)

# 注册订单中心蓝图
from info.modules.orderCenter import orderCenter_blue
app.register_blueprint(orderCenter_blue)

#  注册建群管理蓝图
from info.modules.createQun import createQun_blue
app.register_blueprint(createQun_blue)

