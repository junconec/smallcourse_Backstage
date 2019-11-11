import logging
import pymysql


class Config(object):
    """工程配置信息"""
    # SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    DEBUG = True
    # 云数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://wucongwen:UyTflfZqoITBef6J3pVtrGsalUmznQr6@rm-2ze03u1v79619rwt5o.mysql.rds.aliyuncs.com:3306/kkb-cloud-vipcourse"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class RET(object):
    """结果状态码"""
    PARAERR = 101 # 参数错误
    DBERR = 102 # 数据库错误
    USERERR = 103 # 用户名错误
    PWDERR = 104 # 密码错误
    AUTHERR = 105 # 权限问题
    OK = 200 # 成功


# 本地数据库信息        读写分离
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PW = 'mysql'
MYSQL_PORT = 3306
MYSQL_DB = 'small_class'
MYSQL_TB = 'middle'  # qun_id 跟 customer_id 对应表
