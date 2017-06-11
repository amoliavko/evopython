from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class InputName(Form):
    name = TextField('name', validators=[Required()])
