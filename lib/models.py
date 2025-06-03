

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date

from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Forecast(Base):
     
    __tablename__ = 'forecasts'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    condition = Column(String, nullable=False)  
    
    weather_records = relationship("WeatherRecord", back_populates="forecast")

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    temperature = Column(Float)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    condition = Column(String)
    
    weather_records = relationship("WeatherRecord", back_populates="location")
    
class WeatherRecord(Base):
   
    __tablename__ = "weather_records"
    
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    forecast_id = Column(Integer, ForeignKey("forecasts.id"))
    temperature = Column(Float)
    feels_like = Column(Float)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    pressure = Column(Integer)
    recorded_at = Column(DateTime, default=datetime.utcnow)

    location = relationship("Location", back_populates="weather_records")
    forecast = relationship("Forecast", back_populates="weather_records")