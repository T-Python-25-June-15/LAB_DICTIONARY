Weather_dictionary = {} 
def User_Weather():
    user_city = input("Please enter the city: ")
    if user_city == "":
        return "Invalid, you need to type a city"
    user_date = input("Please enter the date: ")
    if user_date == "":
        return "Invalid, You need to type a date"
    user_temperature = input("Please enter the temperature: ")
    if not user_temperature.isdigit():
        return "Invalid, You need to type a temperature"
    user_humidity = int(input("Please enter the humidity: "))
    if user_humidity < 0 or  user_humidity > 100:
        return "Invalid, The humidity should be between 0 and 100"
    user_weather_condition = input("Please enter the weather condition: ")
    if user_weather_condition.lower() != "rainy" and user_weather_condition.lower() != "sunny" and user_weather_condition.lower() != "windy" and user_weather_condition.lower() != "cloudy" and user_weather_condition.lower() != "snowy" and user_weather_condition.lower() != "stormy":
        return "Invalid, you need to type the weather condition for example (sunny , windy, cloudy ,stormy, rainy or snowy)"
    #in here i add something that wasn't ask but i felt like it: i made it check if there is a city with this date that was added before to stop him from doing so because he/she should use the update function
    if user_city in Weather_dictionary and user_date in Weather_dictionary[user_city]:
        return f"There is a weather with this city ({user_city}) by this date {user_date}"
    if user_city not in Weather_dictionary:
        Weather_dictionary[user_city] = {}
    Weather_dictionary[user_city][user_date] = {}
        
    Weather_dictionary[user_city][user_date]['temperature'] = user_temperature
    Weather_dictionary[user_city][user_date]['humidity'] = user_humidity
    Weather_dictionary[user_city][user_date]['condition'] = user_weather_condition 
    return Weather_dictionary

def Update():
    user_city = input("Please enter the city: ")
    if user_city == "":
        return "Invalid, you need to type a city"
    user_date = input("Please enter the date: ")
    if user_date == "":
        return "Invalid, You need to type a date"
    if user_city not in Weather_dictionary or user_date not in Weather_dictionary[user_city]:
        return f"There isn't a weather with this city ({user_city}) by this date {user_date}. You need to inserted the date and the city to update."
    user_temperature = input("Please enter the temperature: ")
    if not user_temperature.isdigit():
        return "Invalid, You need to type a temperature"
    user_humidity = int(input("Please enter the humidity: "))
    if user_humidity < 0 or  user_humidity > 100:
        return "Invalid, The humidity should be between 0 and 100"
    user_weather_condition = input("Please enter the weather condition: ")
    if user_weather_condition.lower() != "rainy" and user_weather_condition.lower() != "sunny" and user_weather_condition.lower() != "windy" and user_weather_condition.lower() != "cloudy" and user_weather_condition.lower() != "snowy" and user_weather_condition.lower() != "stormy":
        return "Invalid, you need to type the weather condition for example (sunny , windy, cloudy ,stormy, rainy or snowy)"
    
        
    Weather_dictionary[user_city][user_date]['temperature'] = user_temperature
    Weather_dictionary[user_city][user_date]['humidity'] = user_humidity
    Weather_dictionary[user_city][user_date]['condition'] = user_weather_condition
    print(f"you updated the weather for {user_city}") 
    return Weather_dictionary

def Query(city_name):
    if city_name in Weather_dictionary:
        print(Weather_dictionary[city_name])
    else:
        print(f"There isn't weather for this city")

def delete():
    user_city = input("Please enter the city: ")
    if user_city not in Weather_dictionary:
        return "You can't delete this city because it not inserted"
    user_date = input("Please entry the date that you want to delete: ")
    if user_date not in Weather_dictionary[user_city]:
        return f"There is no weather with this date {user_date} in this city {user_city}"
        
    del Weather_dictionary[user_city][user_date]
    return "it deleted"

user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")
print("-"*15)
while user_input != "exit":
    if user_input == "1":
        print(User_Weather())
        print("-"*15)
        print()
        user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")
    elif user_input == "2":
        print(Update())
        print("-"*15)
        print()
        user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")
    elif user_input == "3":
        user_city = input("Please entry the city that you want to query: ")
        Query(user_city)
        print("-"*15)
        print()
        user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")
    elif user_input == "4":
        print(delete())
        print("-"*15)
        print()
        user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")
    else:
        print("invaild input")
        print()
        user_input = input("1)put a new weather \n 2)update the weather \n 3)Query the weather by City \n 4)delete the weather \n to exit type 'exit': ")



        
        
    
