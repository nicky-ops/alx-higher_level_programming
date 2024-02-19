#!/usr/bin/python3
"""
This module defines the class City that inherits from the Base class from
the declarative base function
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    This class defines a model City that inherits from Base
    It links to the MySQL table cities

    CLASS ATTRIBUTES:
    id - represents a column of auto-generated, unique integer
    name - column of a string to store the state name
    state_id - represents a column of an integer, can't be null and is a foreign key to states.id

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    def __repr__(self):
        """
        string representation of an object
        """
        return f"<User(id={self.id}, name={self.name})>"
