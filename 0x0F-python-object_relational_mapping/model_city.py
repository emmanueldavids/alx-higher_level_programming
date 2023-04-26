#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

"""
City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated, unique integer, 
can’t be null and is a primary key
class attribute name that represents a column of a string of 128 characters and 
can’t be null
class attribute state_id that represents a column of an integer, can’t be null and is 
a foreign key to states.id
You must use the module SQLAlchemy 
"""

class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'),nullable=False)