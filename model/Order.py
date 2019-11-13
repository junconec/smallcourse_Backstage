# -*- coding:utf-8 -*-
from info import db


# 订单表
class Order(db.Model):
    __tablename__ = 'vip_order'

    id = db.Column(db.Integer, primary_key=True) # 类型 是否是主键
    # 订单编号
    no = db.Column(db.String(32))
    # 订单类型  线上线下
    type = db.Column(db.Integer)
    # 课程id
    course_id = db.Column(db.Integer)
    # 课程类型
    course_type = db.Column(db.Integer)
    # 课程编号
    course_code = db.Column(db.String(32))
    # 班次id
    class_id = db.Column(db.Integer)
    # 渠道id
    channel_id = db.Column(db.Integer)
    # 渠道code
    channel_code = db.Column(db.String(32))
    # 商品id
    item_id = db.Column(db.Integer)
    # 商品名称
    item_name = db.Column(db.String(32))
    # 商品班级id
    item_sku_id = db.Column(db.Integer)
    # 商品班级名称
    item_sku_name = db.Column(db.String(32))
    # 用户id
    user_id = db.Column(db.Integer)
    # 销售id
    seller_id = db.Column(db.Integer)
    # 销售名称
    seller_name = db.Column(db.String(32))
    # 用户池id
    track_id = db.Column(db.Integer)
    # 用户池名称
    track_name = db.Column(db.String(32))
    # 微信唯一标识
    unionid = db.Column(db.String(32))
    # 微信openid
    openid = db.Column(db.String(32))
    # 昵称
    nickname = db.Column(db.String(32))
    # 头像
    headimgurl = db.Column(db.String(64))
    # 原价格
    price = db.Column(db.Numeric(2))
    # 积分
    points = db.Column(db.Integer)
    # 优惠券
    coupon = db.Column(db.Numeric(2))
    # 折扣
    discount = db.Column(db.Numeric(2))
    # 实际价格
    amount = db.Column(db.Numeric(2))
    # 支付状态
    status = db.Column(db.Integer)
    # 添加好友时间
    add_friend_time = db.Column(db.Integer)
    # 备注
    remark = db.Column(db.String(64))
    # 调班后班级id
    modify_class_id = db.Column(db.Integer)
    # 修改班级时间
    modify_class_time = db.Column(db.Integer)
    # 创建时间
    create_time = db.Column(db.Integer)
    # app_code
    app_code = db.Column(db.String(32))
    # 支付时间
    pay_time = db.Column(db.Integer)
    # 更新时间
    update_time = db.Column(db.DateTime)
    # 订单id
    out_order_id = db.Column(db.Integer)
    # 芝士分期课程id
    cheese_id = db.Column(db.Integer)
    # 开发者ID(AppID)
    appid = db.Column(db.String(64))
    # 微信唯一标识
    app_openid = db.Column(db.String(64))
    # 权重二维码
    qr_code = db.Column(db.String(128))


    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Order %r>' % self.orderName