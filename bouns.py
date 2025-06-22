weather = { 

 }

for i in range(1): 

   city= input("cityname: ")
   date = input("date:") 
   temperature = input("temperature:")
   humidity = input("humidity")
   weather_condition = input("weather_condition:")

   weather = { 
       "city":city,
       "date" :date,
       "temperature" :temperature,
       "humidity" :humidity,
       "weather_condition" : weather_condition
        }


 
weather[city][date] = {
    "temperature": temperature,
    "humidity": humidity,
    "condition": weather_condition
    }

def query_city():
   city2=input("Enter the city: ")
   if city2 == weather[city]:
      print(weather.values)
      
 