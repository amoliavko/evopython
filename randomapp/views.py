from randomapp import app, db
from randomapp.model import Table
from flask import render_template, redirect, request
from randomapp.forms import InputName
import random


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputName()
    if request.method == 'POST':
        if request.form['submit'] == 'Добавить имя':
            if form.name.data:
                return render_template('/success.html', result=[1,2,3])

        elif request.form['submit'] == 'Выбрать случайных победителей':
            id_list = []
            result = [11, 22]
            for i in db.session.query(Table.name):
                id_list.append(i)
            #
            # if len(id_list) <= 3:
            #     for i in id_list:
            #         result.append(i[-1])
            #
            # else:
            #     while len(result) <= 3:
            #         nm = random.choice(id_list)[-1]
            #         if nm not in result:
            #             result.append(nm)
            return str(id_list)
 #           return render_template('/success.html', result=result)

    return render_template('index.html', form=form)
