from sqlalchemy import create_engine, MetaData, Table, Column, VARCHAR, INTEGER
from config import SQLALCHEMY_DATABASE_URI
from randomapp import db

db.create_all()
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# db.create_all()
#
#
#
# meta = MetaData(bind=engine, reflect=True)
#
# print(engine, "\n", meta)
#
# table_1 = Table('count', meta,
#                 Column('id', INTEGER),
#                 Column('Name', VARCHAR))