from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import warnings
import logging
from logging.handlers import RotatingFileHandler

from config import config

warnings.filterwarnings("ignore")


#  导入要迁移的数据库模型
from info import app, db


manager = Manager(app)
# 数据库迁移 配置
Migrate(app, db)
manager.add_command('db', MigrateCommand)

from model.Order import Order
from model.VipSellerQrcode import VipSeller
# from model.Middle import Middle
def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


if __name__ == '__main__':
    #  数据库迁移 需要改为 manager.run()
    # db.create_all()
    # manager.run()

    # 项目启动 需要改为app.run()
    app.run()

