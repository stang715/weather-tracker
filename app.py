from services.weather_services import store_weather_data
import time
import requests

def run_weather_tracker():
    hours = int(input("How many hours do you want to keep track of the weather?"))

    print(hours)

    api = input("enter your api id")
    # hard coded the lat and lon for these 3 cities
    urlList = {'chino hills': 'https://api.openweathermap.org/data/2.5/forecast?lat=33.9926803&lon=-117.760056&limit=1&cnt=3&appid='+api, 
            'seattle': "https://api.openweathermap.org/data/2.5/forecast?lat=47.6038321&lon=-122.330062&limit=1&cnt=3&appid="+api, 
            'houston': "https://api.openweathermap.org/data/2.5/forecast?lat=29.7589382&lon=-95.3676974&limit=1&cnt=3&appid="+api}

    count = 0
    while count < hours:
        for city in urlList: 
            store_weather_data(urlList[city])
        print("Waiting for 1 hour before next request...")
        time.sleep(3600)  # Sleep for 3600 seconds = 1 hour
        count += 1

run_weather_tracker()
