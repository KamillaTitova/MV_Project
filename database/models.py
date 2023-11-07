from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Table_1(Base):

    __tablename__ = 'Table_1'
    __tableargs__ = {
        'comment': ''
    }

    topic_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(128), comment='Наименование темы')
    description = Column(Text, comment='Описание темы')

    def __repr__(self):
        return f'{self.topic_id} {self.name} {self.description}'

