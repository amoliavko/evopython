from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


app = Flask(__name__)
app.config.from_object('config')


class InputName(FlaskForm):
    name = TextField('name', validators=[Required()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputName()
    if form.validate_on_submit():
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)

