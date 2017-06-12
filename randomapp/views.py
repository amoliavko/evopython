from randomapp import app
from flask import render_template
from randomapp.forms import InputName

@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputName()
	return render_template('index.html')

