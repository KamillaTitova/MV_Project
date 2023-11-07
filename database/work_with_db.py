# from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, declarative_base
# from database.models import DB_Scripts
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_
from sqlalchemy.orm import registry


# Создание базового класса моделе и создание подключения к базе данных SQLite
engine = create_engine('sqlite:///Users/kamillatitova/Library/DBeaverData/workspace6/General/Scripts/scripts.db', echo=True)
meta = MetaData(engine)

db_table = Table('scripts', meta, autoload=True)

conn = engine.connect()
s = select([db_table]).where(db_table.c.authors == '164098')
result = conn.execute(s)

for row in result.fetchall():
   print(row)
# with engine.connect() as connection:
#     result = connection.execute(text('SELECT * FROM users'))
#
#     for row in result:
#         print(row)

# metadata = MetaData(bind=engine)


# Определение модели таблицы
# class DB_Scripts(Base):
#     __table__ = Table('scripts', MetaData, autoload=True)

# Создание сессии для использования таблицы
# session = create_session(bind=engine)
#
# estlist = session.query(Tests).all()

# for test in testlist:
#     testauthor = session.query(Users).filter_by(id=test.author_id).first()
#     if testauthor:
#         print ("Test Name: {}, Test Author: {}".format(test.testname, testauthor.fullname)
#     else:
#         print ("Test Name: {}, No author recorded".format(test.testname))