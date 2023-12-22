import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.types import DATE, VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import pool

engine = create_engine(f'postgresql+psycopg2://localhost/CryptoScriptDB', echo=True)

#engine = create_engine(f"sqlite+pysqlite:///{os.path.abspath(os.getcwd())}\\pylounge.db", echo=True)

Base = declarative_base()


class Main(Base):
    __tablename__ = 'scriptstable'
    script_id = Column(Integer, primary_key=True)
    script_name = Column(VARCHAR(60))
    script_code = Column(VARCHAR)
    script_description = Column(VARCHAR(256))
    created_ts = Column(DATE)
    script_author = Column(VARCHAR(250))
    pers_num_author = Column(Integer)

Base.metadata.create_all(engine)