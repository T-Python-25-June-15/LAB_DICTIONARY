
weatherDictionary = {}

def inputWeatherData():
    city = input("Enter city name: ")
    date = input("Enter date mm/dd/yy: ")
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    weather_condition = input("Enter weather Condition: ")

    weatherDictionary[city] = {}
    weatherDictionary[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "weather_condition": weather_condition
    }

def querybByCity():
    foundCity = input("Enter city to found: ")
    if foundCity in weatherDictionary:
        for date,info in weatherDictionary[foundCity].items():
            print(f"""
                City: {foundCity}
                    Date:               {date}
                    Temperature:        {info["temperature"]}
                    Humidity:           {info["humidity"]}
                    Weather condition:  {info["weather_condition"]}
            """)
    else:
        print("No data for this city.")


while True:
    print("""
          --------------------------
        1- Input Weather data
        2- Query City
          --------------------------
""")
    option = (input("select an option: "))
    try:

        if int(option) == 1:
            inputWeatherData()
        if int(option) == 2:
            querybByCity()
    except:
        print("There is no option like that.")

    