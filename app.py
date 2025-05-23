from services.weather_services import store_weather_data
import time
import requests

def run_weather_tracker():
    # check valid hours
    hours = input("How many hours do you want to keep track of the weather? ")
    while not hours.isnumeric():
        print("Hours must be a number!")
        hours = input("How many hours do you want to keep track of the weather? ")

    # convert hours string to integer
    hours = int(hours)

    # check for a valid api
    api = input("Enter your api id: ")
    while not test_api_key(api):
        print("Invalid Api Id!")
        api = input("Enter your api id: ")

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
    
def test_api_key(api):
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=33.9926803&lon=-117.760056&limit=1&cnt=3&appid=" + api
    response = requests.post(url)
    if response.status_code == 200:
        return True
    else:
        return False

run_weather_tracker()
