from randomapp import app, db
from randomapp.model import Table
from flask import render_template, redirect, request
from randomapp.forms import InputName
import random


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputName()
    if request.method == 'POST':
        if request.form['submit'] == 'Добавить имя':
        	return "yes"
    return render_template('index.html', form=form)
