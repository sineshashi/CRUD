from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind= engine)
session = Session()

with session:
    Base.metadata.create_all(engine)