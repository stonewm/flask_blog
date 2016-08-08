# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    # 第一个字段，openid, data is required
    openid = StringField('openid', validators=[DataRequired()])
    
    # 第二个字段，remember_me, 默认为unchecked
    remember_me = BooleanField('remember_me', default=False)




