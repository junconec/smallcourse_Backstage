import logging

import pymysql
from logging.handlers import RotatingFileHandler

class Config(object):
    """工程配置信息"""
    # SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    DEBUG = True
    # 云数据库的配置信息
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/small_class"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://wucongwen:UyTflfZqoITBef6J3pVtrGsalUmznQr6@rm-2ze03u1v79619rwt5o.mysql.rds.aliyuncs.com:3306/kkb-cloud-vipcourse"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
class RET(object):
    """结果状态码"""
    PARAERR = 101 # 参数错误
    DBERR = 102 # 数据库错误
    USERERR = 103 # 用户名错误
    PWDERR = 104 # 密码错误
    AUTHERR = 105 # 权限问题
    OK = 200 # 成功


# 本地数据库信息
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PW = 'mysql'
MYSQL_PORT = 3306
MYSQL_DB = 'small_class'
MYSQL_TB = 'middle'  # 储存群id和订单关系的表


# 云数据库 sql查询配置
# MYSQL_HOST_2 = 'localhost'  # 云数据库host
# MYSQL_USER_2 = 'root'  # 云数据库user
# MYSQL_PW_2 = 'mysql'  # 云数据库pw
# MYSQL_PORT_2 = 3306  # 云数据库port
# # 云数据库第一个库
# MYSQL_DB_1 = 'small_class'  # 第一个库名  （kkb-cloud-vipcourse）
# MYSQL_TB_VIP = 'vip_seller_qrcode'  # vip_seller_qrcode表
#
# # 云数据库第二个库
# MYSQL_DB_2 = 'small_class_2'  # 储存用户的数据库  (kkb-cloud-account)
# MYSQL_TB_2 = 'sys_user'  # 储存用户的表 (sys_user)
# 云数据库 sql查询配置
MYSQL_HOST_2 = 'rm-2ze03u1v79619rwt5o.mysql.rds.aliyuncs.com'  # 云数据库host
MYSQL_USER_2 = 'wucongwen'  # 云数据库user
MYSQL_PW_2 = 'UyTflfZqoITBef6J3pVtrGsalUmznQr6'  # 云数据库pw
MYSQL_PORT_2 = 3306  # 云数据库port
# 云数据库第一个库
MYSQL_DB_1 = 'kkb-cloud-vipcourse'  # 第一个库名  （kkb-cloud-vipcourse）
MYSQL_TB_VIP = 'vip_seller_qrcode'  # vip_seller_qrcode表

# 云数据库第二个库
MYSQL_DB_2 = 'kkb-cloud-account'  # 储存用户的数据库  (kkb-cloud-account)
MYSQL_TB_2 = 'sys_user'  # 储存用户的表 (sys_user)