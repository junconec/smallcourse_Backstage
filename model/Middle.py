# -*- coding:utf-8 -*-
from info import db

# 群与成员关系表
class Middle(db.Model):
    __tablename__ = 'middle'

    id = db.Column(db.Integer, primary_key=True) # 类型 是否是主键
    # 群id
    class_id = db.Column(db.String(128))
    # 成员id
    member_id = db.Column(db.String(128))

    def __init__(self, class_id, member_id):
        self.class_id = class_id
        self.member_id = member_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Order %r>' % self.orderName