#!/usr/bin/python3
""" a python file that contains the class definition of a City class
"""
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
