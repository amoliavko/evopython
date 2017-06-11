from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


from randomapp import views


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'YES'





