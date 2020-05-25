from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from database_connection import  engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Users(Base):

    __tablename__ = 'USERS'

    USER_ID = Column(Integer, primary_key=True)
    FIO = Column(String(100))
    BIARTHDATE = Column(Date)
    EQUIPMENT = Column(Integer)
    HEALTHY = Column(Integer)
    HEIGHT = Column(Float)
    WEIGHT = Column(Float)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()