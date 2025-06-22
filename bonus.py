
weather_data = {}


def printHomePage():
    print("\n======== Weather Data Aggregation Program ======== \n")
    print("1. Input weather data")
    print("2. Query by city")
    print("3. Exit\n")
    print("="* 50)

def addWeatherData():
    city_name = input("City name: ")
    date = input("Date (dd/mm/yyyy): ")
    temp = input("temperature: ")
    humidity = input("humidity: ")
    weather_condition = input("weather condition: ")
    
    # validation ---
    
    # end validation ---
    
    city = {
        "name": city_name,
        "date": date,
        "temp": temp,
        "humidity": humidity,
        "weather_condition": weather_condition
    }
    
    return city

def queryByCity(name:str):
    if name in weather_data:
        print(f"\nName: {weather_data[name]["name"]}")
        print(f"Date: {weather_data[name]["date"]}")
        print(f"Temperature: {weather_data[name]["temp"]}")
        print(f"Humidity: {weather_data[name]["humidity"]}")
        print(f"Weather condition: {weather_data[name]["weather_condition"]}")
    else:
        print("Not Found!.")

def main():
    while True:
        printHomePage()
        user_input = input("Enter your choice: ")
        if user_input.isalpha(): 
            print("number only, try again")
            continue
        
        user_input = int(user_input)
        if user_input == 1:
            new_city = addWeatherData()
            weather_data[new_city["name"]] = new_city
            print("new city added succesfully!.")
            
        elif user_input == 2:
            city_name = input("city name: ")
            queryByCity(city_name)
            
        elif user_input == 3:
            break
        else:
            print("try again!.")
            
main()