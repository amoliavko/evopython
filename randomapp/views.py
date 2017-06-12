from randomapp import app

from flask import render_template, redirect, request
from randomapp.forms import InputName


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputName()
    if form.validate_on_submit():
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)
