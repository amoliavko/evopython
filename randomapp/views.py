from randomapp import app
from flask import render_template, flash, redirect
from randomapp.forms import InputName


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputName()
    if form.validate_on_submit():
        flash(form.name.data)
        return redirect('/success')
    return render_template('index.html', form=form)