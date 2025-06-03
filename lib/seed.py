from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

from models import Base, Forecast, Location, WeatherRecord

# Connect to the database
engine = create_engine("sqlite:///weather.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Clear existing data
session.query(WeatherRecord).delete()
session.query(Location).delete()
session.query(Forecast).delete()
session.commit()

# Seed Forecasts
forecast1 = Forecast(date=date(2025, 6, 2), condition="Sunny")
forecast2 = Forecast(date=date(2025, 6, 3), condition="Cloudy")
forecast3 = Forecast(date=date(2025, 6, 4), condition="Rainy")
forecast4 = Forecast(date=date(2025, 6, 5), condition="Thunderstorms")
forecast5 = Forecast(date=date(2025, 6, 6), condition="Clear Skies")

session.add_all([forecast1, forecast2, forecast3, forecast4, forecast5])
session.commit()

# Seed Locations
locations = [
    Location(name="Nairobi", date="2025-06-02", temperature=25.3, humidity=60, wind_speed=5.5, condition="Sunny"),
    Location(name="Mombasa", date="2025-06-02", temperature=30.0, humidity=75, wind_speed=7.2, condition="Hot and Humid"),
    Location(name="Kisumu", date="2025-06-02", temperature=27.5, humidity=68, wind_speed=4.0, condition="Partly Cloudy"),
    Location(name="Eldoret", date="2025-06-02", temperature=22.1, humidity=55, wind_speed=6.1, condition="Cool and Breezy"),
    Location(name="Nakuru", date="2025-06-02", temperature=23.8, humidity=62, wind_speed=5.0, condition="Mild"),
    Location(name="Garissa", date="2025-06-02", temperature=35.0, humidity=40, wind_speed=8.3, condition="Hot and Dry"),
    Location(name="Meru", date="2025-06-02", temperature=21.5, humidity=70, wind_speed=3.5, condition="Foggy Morning"),
    Location(name="Kitale", date="2025-06-02", temperature=20.0, humidity=80, wind_speed=4.2, condition="Rain Showers"),
    Location(name="Thika", date="2025-06-02", temperature=24.7, humidity=58, wind_speed=5.7, condition="Clear Skies"),
    Location(name="Machakos", date="2025-06-02", temperature=26.0, humidity=64, wind_speed=5.1, condition="Warm"),
    Location(name="Nyeri", date="2025-06-02", temperature=19.5, humidity=72, wind_speed=3.8, condition="Misty"),
    Location(name="Lamu", date="2025-06-02", temperature=32.2, humidity=80, wind_speed=6.5, condition="Tropical Heat"),
]

session.add_all(locations)
session.commit()

# Seed Weather Records
records = [
    WeatherRecord(
        location_id=locations[0].id,
        forecast_id=forecast1.id,
        temperature=25.3,
        feels_like=27.0,
        humidity=60,
        wind_speed=5.5,
        pressure=1012,
        recorded_at=datetime(2025, 6, 2, 9, 0)
    ),
    WeatherRecord(
        location_id=locations[1].id,
        forecast_id=forecast2.id,
        temperature=30.0,
        feels_like=33.5,
        humidity=75,
        wind_speed=7.2,
        pressure=1008,
        recorded_at=datetime(2025, 6, 3, 9, 0)
    ),
    WeatherRecord(
        location_id=locations[2].id,
        forecast_id=forecast3.id,
        temperature=27.5,
        feels_like=29.0,
        humidity=68,
        wind_speed=4.0,
        pressure=1010,
        recorded_at=datetime(2025, 6, 4, 9, 0)
    ),
    WeatherRecord(
        location_id=locations[3].id,
        forecast_id=forecast4.id,
        temperature=22.1,
        feels_like=22.5,
        humidity=55,
        wind_speed=6.1,
        pressure=1015,
        recorded_at=datetime(2025, 6, 5, 9, 0)
    ),
    WeatherRecord(
        location_id=locations[4].id,
        forecast_id=forecast5.id,
        temperature=23.8,
        feels_like=24.2,
        humidity=62,
        wind_speed=5.0,
        pressure=1013,
        recorded_at=datetime(2025, 6, 6, 9, 0)
    )
]

session.add_all(records)
session.commit()

print("✅ Seeding complete!")