# -*- coding:utf-8 -*-
from info import db


# 订单表
class VipSeller(db.Model):
    __tablename__ = 'vip_seller_qrcode'

    id = db.Column(db.Integer, primary_key=True)  # 类型 是否是主键

    # 班次id
    class_id = db.Column(db.Integer)
    # name
    name = db.Column(db.String(255))
    # 权重二维码
    qr_code = db.Column(db.String(128))
    # pv
    pv = db.Column(db.Integer)
    # uv
    uv = db.Column(db.Integer)
    # press
    press = db.Column(db.Integer)
    # weight
    weight = db.Column(db.Integer)
    # create_by
    create_by = db.Column(db.Integer)
    # create_time
    create_time = db.Column(db.Integer)
    # sales_id
    sales_id = db.Column(db.Integer)
    # seller_id
    seller_id = db.Column(db.Integer)
    # subject_num
    subject_num = db.Column(db.String(32))
    # status
    status = db.Column(db.Integer)
    # title
    title = db.Column(db.String(255))
    # description
    description = db.Column(db.String(255))
    # bottom
    bottom = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<VipSeller %r>' % self.orderName