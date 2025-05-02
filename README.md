How to run the application:
1. run weather_repository first to create database. To do this type this in console: python weather_repository.py
2. run app.py. To do this type: python app.py

How to run unit test
1. run unit_test.py by typing: python unit_test.py in console.

How weather tracker works
1. On app run, you will be prompted to input the number of hours to track the weather. 
    - This will call the api for each city every hours up to the inputed amount of hours
    - Then you will be asked to input the your api key.
2. The app will hit the endpoint 3 times for each of our 3 cities.
    - The cities will be Chino Hills, Seattle, and Houston.
3. The json response from the query will be saved in a data model.
4. The data model will be added to a list of models which will be commited to the db at the end

Why did I implement it this way
1. The database is ran first to create a place to store our data as per the specifications.
    - I handled the edge cases of when a database has already been created and/or columns created and filled
    - I also logged these steps using print becuase I found print to be the most straightfoward and there was not time to write a logging service
2. I used user input for the amount of hours to run this application
    - I felt that querying every hour would be less stressful for the api service (maybe?)
    - This will fullfill the requirement for querying  at regular intervals
3. I asked for the user api 
    - I do not feel that it is secure to share my api
4. I hard coded the cities
    - I used their geo api to get the longitude and latitude of the cities I wanted. However I did not know if we were allowed to do this.
        - Therefore I hard coded the cities.
    - if I can use the geo api, I would have used a user input to ask for city names, then quiered for the cities and saved the longitudes and latitudes to be used in the weather api
5. I commit to the database at the end of each for loop so that I can limit the amount of commits.

Feel free to ask me any further questions or for me to elaborate.