# -*- coding:utf-8 -*-
from flask import Blueprint

orderCenter_blue = Blueprint("orderCenter",__name__,url_prefix='/orderCenter')

from . import views