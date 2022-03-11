from unicodedata import numeric
from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

#Creating the profile model.
class Profile(Base):
    __tablename__ = 'Profile'

    id = Column(Integer, primary_key=True, autoincrement=True) #Autoincreament will automatically generate id for us.
    checked = Column(Boolean)
    name = Column(String)
    type = Column(String)
    age = Column(Numeric)
    description = Column(String)
    date = Column(DateTime)

    def __repr__(self):
        return f"{self.name} {id}"