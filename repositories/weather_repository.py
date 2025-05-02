import mysql.connector
import os

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root"
)

mycursor = mydb.cursor(buffered=True)

import mysql.connector
from mysql.connector import errorcode

try:
    mycursor.execute("USE weather_db")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist. Creating database...")
        mycursor.execute("CREATE DATABASE weather_db")
        mycursor.execute("USE weather_db")
    else:
        print(f"There was an error while trying to use weather_db: {err}")

# Now create the table (if it doesn't already exist)
try:
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            temp FLOAT, 
            feels_like FLOAT, 
            temp_min FLOAT, 
            temp_max FLOAT, 
            pressure FLOAT, 
            humidity FLOAT
        )
    """)
except mysql.connector.Error as err:
    print(f"Failed to create table: {err}")

"""
Check if a table exists
"""
def insert_weather_data(mycursor, mydb, weather_data):
    try:
        query = """
        INSERT INTO weather (temp, feels_like, temp_min, temp_max, pressure, humidity)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        for weather in weather_data:
            mycursor.execute(query, (
                weather.temp,
                weather.feels_like,
                weather.temp_min,
                weather.temp_max,
                weather.pressure,
                weather.humidity
            ))
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error while inserting weather data: {err}")
