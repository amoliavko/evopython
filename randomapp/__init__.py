from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config.from_object('config')

#db = SQLAlchemy(app)
#heroku = Heroku(app)

from randomapp import views



@app.route('/', methods=['GET', 'POST'])
def index():
    return 'YES'


