from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class InputName(Form):
    name = TextField('name', validators=[Required()])


@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputName()
	if request.method == 'POST':
		if form.validate_on_submit():
			return render_template('index.html', form=form)


