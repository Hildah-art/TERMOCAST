from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  Forecast, Location  
from tabulate import tabulate
engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all cities
def fetch_cities():
    locations = session.query(Location).all()
    if not locations:
        print("No cities found.")
        return
    table = []
    headers = ["ID", "Name", "Date", "Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Condition"]
    for location in locations:
        table.append([
            location.id,
            location.name,
            location.date,
            location.temperature,
            location.humidity,
            location.wind_speed,
            location.condition
        ])
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
# Show a specific city
def get_city():
    city_id = input("Enter City ID: ")
    city = session.query(Location).filter_by(id=city_id).first()
    if city:
        # print(f" Name: {location.name}, Date: {location.date}, Temperature: {location.temperature}, Humidity: {location.humidity}, Windspeed: {location.wind_speed}, Condition: {location.condition}")
        print(f"Name: {city.name},Temperature : {city.temperature}, Condition :{city.condition}")
    else:
        print("City not found.")

# Update city info (admin or seed.py use case)
def update_city():
    city_id = input("Enter City ID: ")
    city = session.query(Location).filter_by(id=city_id).first()
    if city:
        name = input("New name: ")
        country = input("New country: ")
        population = input("New population: ")
        city.name = name
        city.country = country
        city.population = population
        session.commit()
        print("City updated successfully.")
    else:
        print("City not found.")

# Delete a city (only if needed)
def delete_city():
    city_id = input("Enter City ID to delete: ")
    city = session.query(Location).get(city_id)
    if city:
        session.delete(city)
        session.commit()
        print("City deleted.")
    else:
        print("City not found.")

# Fetch all forecasts
def fetch_forecasts():
    forecasts = session.query(Forecast).all()
    if not forecasts:
        print("No forecasts available.")
        return
    table = []
    headers = ["ID", "Date", "Condition", "Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "City ID"]
    for forecast in forecasts:
        table.append([
            forecast.id,
            forecast.date,
            forecast.condition,
            forecast.temperature,
            forecast.humidity,
            forecast.wind_speed,
            forecast.city_id
        ])
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Get forecast by city
def get_forecast_by_city():
    city_name = input("Enter city name: ")
    city = session.query(Location).filter_by(name=city_name).first()
    if city:
        forecasts = session.query(Forecast).filter_by(city_id=city.id).all()
        if forecasts:
            table = []
            headers = ["Date", "Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)"]
            for f in forecasts:
                table.append([f.date, f.temperature, f.humidity, f.wind_speed])
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No forecasts available for this city.")
    else:
        print("City not found.")


# Delete forecast entry
def delete_forecast():
    forecast_id = input("Enter Forecast ID to delete: ")
    forecast = session.query(Forecast).get(forecast_id)
    if forecast:
        session.delete(forecast)
        session.commit()
        print("Forecast deleted.")
    else:
        print("Forecast not found.")