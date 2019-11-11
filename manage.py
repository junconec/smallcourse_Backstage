from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import warnings

from info import app, db

warnings.filterwarnings("ignore")


#  导入要迁移的数据库模型



manager = Manager(app)
# 数据库迁移 配置
Migrate(app, db)
manager.add_command('db', MigrateCommand)

from model.Order import Order
# from model.Middle import Middle


if __name__ == '__main__':
    #  数据库迁移 需要改为manager.run()
    # db.create_all()
    # manager.run()

    # 项目启动 需要改为app.run()
    app.run()
