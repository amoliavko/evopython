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
            if form.name.data == '':
                return render_template("/index.html", form=form, error=form.name.data)
            elif Table.query.filter_by(name=form.name.data).first() is None:
                n = Table(name=form.name.data)
                db.session.add(n)
                db.session.commit()
                return render_template("/index.html", form=form, succuss_add=form.name.data)
            else:
                return render_template("/index.html", form=form, error_add_already=form.name.data)

        elif request.form['submit'] == 'Удалить имя':
            if form.name.data == '':
                return render_template("/index.html", form=form, error=form.name.data)
            elif Table.query.filter_by(name=form.name.data).first():
                    Table.query.filter(Table.name == form.name.data).delete()
                    db.session.commit()
                    return render_template("/index.html", form=form, succuss_del=form.name.data)
            else:
                return render_template("/index.html", form=form, error_del='error')

        elif request.form['submit'] == 'Выбрать случайных победителей':
            id_list = []
            result = []
            for i in db.session.query(Table.name):
                id_list.append(i)

            if len(id_list) <= 3:
                for i in id_list:
                    result.append(i[-1])
            else:
                while len(result) < 3:
                    nm = random.choice(id_list)[-1]
                    if nm not in result:
                        result.append(nm)
            return render_template('/success.html', result=result)

        elif request.form['submit'] == 'Повторить':
                return render_template('/index.html', form=form)

    return render_template('/index.html', form=form)
