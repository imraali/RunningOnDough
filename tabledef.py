from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
########################################################################
        
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column('id', Integer, primary_key = True)
    name = Column(String(100))
    flight = Column(Integer)
    transport = Column(Integer)
    food = Column(Integer)
    entertainment = Column(Integer)
    living = Column(Integer)

    def __init__(self, name, flight, transport, food, entertainment, living):
        """"""
        self.name = name
        self.flight = flight
        self.transport = transport
        self.food = food
        self.entertainment = entertainment
        self.living = living
#        self.dates = dates
 
# create tables
Base.metadata.create_all(engine)
