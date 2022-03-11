from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Connect with the database.
engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind= engine)
session = Session()