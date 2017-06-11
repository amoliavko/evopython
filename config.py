import os

CSRF_ENABLED = True
SECRET_KEY = 'myk433eyforf346laskJJ80app'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/names_database'


