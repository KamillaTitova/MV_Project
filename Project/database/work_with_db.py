from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_decl import Base, Main
import psycopg2


# Создание базового класса моделе и создание подключения к базе данных SQLite
engine = create_engine(f'postgresql+psycopg2://localhost/CryptoScriptDB', echo=True)
session = sessionmaker(bind=engine)

s = session()

for script_code, script_id in s.query(Main.script_code, Main.script_id).filter(Main.script_id == 1):
   print(script_code)

# def showScript():
#    for Script_code, Script_ID in s.query(Main.Script_code, Main.Script_ID).filter(Main.Script_ID == 1):
#       print(Script_code)
#    return render_template('main.html', Script_code=Script_code)
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