import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///users.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("test","test","test","test","test","test")
session.add(user)
 
user = User("test2","test2","test2","test2","test2","test2")
session.add(user)
 
user = User("test3","test3","test3","test3","test3","test3")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
