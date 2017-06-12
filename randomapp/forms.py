from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


class InputName(FlaskForm):
    name = TextField('name', validators=[Required()])

