
weather_data = {}

def weatherSet (city:str , date:str , temperature:int , humidity:int , condition:str):
     if city not in weather_data:
          weather_data[city] = {}

     weather_data[city][date] = {
                "temperature" : temperature,
                "humidity" : humidity,
                "condition" : condition
     }
           
       

def weatherGet (city):
     if city in weather_data:
          print(f"The weather for {city}: ")
          for date , info in weather_data[city].items():
               print(f"- Date: {date}")
               print(f"  Temperature: {info['temperature']}°")
               print(f"  Humidity: {info['humidity']}%")
               print(f"  Condition: {info['condition']}")
               print()

     else:
          print("City not found")
     


while True:
    print("-" * 24)
    print("Weather Data Aggregation")
    print("-" * 24)
    print()
    print("# Options: ")
    print("1. add")
    print("2. search")
    print("3. exit")

    option = int(input("Choose what you want: "))



    match option:
         case 1:
              city = input("Enter the city: ").strip().capitalize()
              

              dateInput =input("Enter the date (YYYY-MM-DD): ")
              if ( len(dateInput) == 10 and
                 dateInput[4] == "-" and
                 dateInput[7] == "-" and
                 dateInput[:4].isdigit() and
                 dateInput[5:7].isdigit() and
                 dateInput[8:].isdigit()):
                   date = dateInput
              else:
                   print("Invalid input, it's not like the format YYYY-MM-DD.")
                   print()
                   print()
                   continue


              temperatureInput = input("Enter the temperature: ")
              if temperatureInput.isdigit():
                   temperature = int(temperatureInput)
              else:
                   print("Invalid input, it must be a number.")
                   print()
                   print()
                   continue


              humidityInput = input("Enter the humidity: ")
              if humidityInput.isdigit():
                   humidity = int(humidityInput)
              else:
                   print("Invalid input, it must be a number.")
                   print()
                   print()
                   continue


              conditionInput = input("Enter the weather condition: ").strip().lower()
              if conditionInput in ("sunny" , "cloudy" , "rainy" , "windy" , "stormy" , "foggy" , "drizzle" ,
                                        "snowy" , "hot" , "cold" , "humid" , "clear" ,"dusty" , "thunderstorm" ):
                   condition = conditionInput
              else:
                   print("Invalid input, you should write the condition of the weather only.")
                   print()
                   print()
                   continue
                   

              weatherSet(city , date , temperature , humidity , condition)
              print()
              print("Data saved successfully.")
              print()
              print()

         case 2:
              city = input("Enter the city: ")
              weatherGet(city)

         case 3:
              print("Thank you.")
              break
        
         case _:
              print("Invalid input.")