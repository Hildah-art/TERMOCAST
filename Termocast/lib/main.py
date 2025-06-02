

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine('sqlite:///lib/weather_.db')

Session = sessionmaker(bind = engine)
session = Session()