# Weather Data Aggregation
# Initialize variables 
weather_dictionary:dict = {}
user_condition:bool = True
counter:int = 0

def create_city_info(city:str, date:str, temp:str, humidity:str, condition:str):
    #This function adds weather data to the dictonary
    weather_dictionary[city] = {"Date":date,
                                "Temperature": temp,
                                "Humidity": humidity,
                                "weatherCondition":condition}

while user_condition:
    user_input:str = input("What do you want to do?\n1. Create a new record. \n2. Query by city. \n3. Exit.\nYour choice? ")
    if user_input == "1":
        user_input_city:str = input("City Name: ")
        user_input_date:str= input("Date (YYYY-MM-DD): ")
        user_input_temperature:str = input("Temperature: ")
        user_input_humidity:str = input("Humidity: ")
        user_input_weather_condition:str = input("Weather Condition: ")
        if not user_input_temperature.isdigit(): 
            print("Invalid number for temperature!")
        elif not user_input_humidity.isdigit(): 
            print("Invalid number for humidity!")
        else:
            create_city_info(user_input_city,user_input_date,user_input_temperature,user_input_humidity,user_input_weather_condition)
    elif user_input == "2":
        user_query_input = input("Enter the city name to view its weather data: ")
        if user_query_input in weather_dictionary:
            print(f"""
                  City              :   {user_query_input}
                  Date              :   {weather_dictionary[user_query_input]["Date"]}  
                  Temperature       :   {weather_dictionary[user_query_input]["Temperature"]} 
                  Humidity          :   {weather_dictionary[user_query_input]["Humidity"]}
                  Weather Condition :   {weather_dictionary[user_query_input]["weatherCondition"]}""")
        else:
            print(f"Sorry, there is no information available for the city you chose ( {user_query_input} ).")
    elif user_input == "3":
        user_condition = False
    else:
        print("Invalid choice.")

        
    
    