# -*- coding:utf-8 -*-
from flask import Blueprint

createQun_blue = Blueprint("createQun",__name__,url_prefix='/createQun')

from . import views
