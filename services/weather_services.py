import requests
import mysql.connector
import os
from models.weather_dto import *
from repositories.weather_repository import *

def store_weather_data(cityApi):
    url = cityApi
    response = requests.post(url)
    result = []

    city = response.json()['city']['name']
    print(f"\nStoring the 5 day weather forecast for {city}.")

    for r in response.json()['list']:
        date_time = r['dt_txt']
        temp = r['main']['temp']
        feels_like = r['main']['feels_like']
        temp_min = r['main']['temp_min']
        temp_max = r['main']['temp_max']
        pressure = r['main']['pressure']
        humidity = r['main']['humidity']
        weather = MainWeather(temp, feels_like, temp_min, temp_max, pressure, humidity)
        result.append(weather)
        print(f"The 3 hour forecast for {date_time} is: Temp: {temp}, Feels Like: {feels_like}, Humidity: {humidity}")

    insert_weather_data(mycursor, mydb, result)

    mycursor.execute("SELECT COUNT(*) FROM weather")
    row_count = mycursor.fetchone()
    print(f"Current number of rows in weather table: {row_count[0]}")
