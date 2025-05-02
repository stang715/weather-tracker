import requests
import mysql.connector
import os
from models.weather_dto import *
from repositories.weather_repository import *

# current city
# http://api.openweathermap.org/geo/1.0/direct?q=chino%20hills&limit=1&appid=01952b2c2d99bab838ea5c82988c6b19

#actual forecast url
# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&limit=1&appid={appid}

# chino hills
# https://api.openweathermap.org/data/2.5/forecast?lat=33.9926803&lon=-117.760056&limit=1&cnt=5&appid=01952b2c2d99bab838ea5c82988c6b19
# seattle
# https://api.openweathermap.org/data/2.5/forecast?lat=47.6038321&lon=-122.330062&limit=1&cnt=5&appid=01952b2c2d99bab838ea5c82988c6b19
# houston
# https://api.openweathermap.org/data/2.5/forecast?lat=29.7589382&lon=-95.3676974&limit=1&cnt=5&appid=01952b2c2d99bab838ea5c82988c6b19
 

def store_weather_data(cityApi):
    city = cityApi[0]
    url = cityApi[1]
    response = requests.post(url)
    result = []

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
