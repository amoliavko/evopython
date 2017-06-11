from sqlalchemy import Column, INTEGER, VARCHAR
from randomapp import db


class Table(db.Model):
    __tablename__ = 'names'
    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(VARCHAR)

    def __repr__(self):
        return 'Name is {}'.format(self.name)
