import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.types import DATE, VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import pool

engine = create_engine('sqlite:////Users/kamillatitova/Desktop/Project_MV/Project/pylounge.db', echo=True)

#engine = create_engine(f"sqlite+pysqlite:///{os.path.abspath(os.getcwd())}\\pylounge.db", echo=True)

Base = declarative_base()


class Info(Base):
    __tablename__ = 'InfoTable'

    Table_ID = Column(Integer, primary_key=True)
    Name_DB = Column(VARCHAR(250))
    Info = relationship("Main") # 1 ко многим


class Main(Base):
    __tablename__ = 'MainTable'
    Script_ID = Column(Integer, primary_key=True)
    Table_id = Column(Integer, ForeignKey("InfoTable.Table_ID"))
    Script_code = Column(VARCHAR(250))
    Created_ts = Column(DATE)
    Author = Column(VARCHAR(250))
    Table = relationship("Info")


Base.metadata.create_all(engine)