from randomapp import app, db
from config import SQLALCHEMY_DATABASE_URI

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'YES '+ SQLALCHEMY_DATABASE_URI
