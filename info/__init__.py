# -*- coding: UTF-8 -*-
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PW, MYSQL_DB, MYSQL_TB

app = Flask(__name__)

# 配置
app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)


# 创建本地数据库对象
conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PW, db=MYSQL_DB)
cur = conn.cursor()


# 注册主页蓝图
from info.modules.index import index_blue
app.register_blueprint(index_blue)

# 注册订单中心蓝图
from info.modules.orderCenter import orderCenter_blue
app.register_blueprint(orderCenter_blue)

#  注册建群管理蓝图
from info.modules.createQun import createQun_blue
app.register_blueprint(createQun_blue)

