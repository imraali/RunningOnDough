import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///users.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("Mru",2000,20,100,80,100)
session.add(user)
 
user = User("Swetlika",1500,50,75,300,50)
session.add(user)
 
user = User("Imra",1750,40,80,1300,60)
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
