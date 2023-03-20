#!/usr/bin/python3
""" a python file that contains the class definition of a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    from relationship_city import City
    cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, name):
        self.name = name
