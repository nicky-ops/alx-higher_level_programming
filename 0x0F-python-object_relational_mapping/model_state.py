#!/usr/bin/python3
"""
This module defines the class State that inherits from the Base class from 
the declarative base function
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """
    This class defines a model State that inherits from Base
    It links to the MySQL table states
    
    CLASS ATTRIBUTES:
    id - represents a column of auto-generated, unique integer
    name - column of a string to store the state name

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


    def __repr__(self):
        """
        string representation of an object
        """
        return f"<User(id={self.id}, name={self.name})>"
