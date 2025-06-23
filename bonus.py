weather_Data={}






def input_weather_Data(city_name:str, date:str, temperature:str, humidity:str, weather_condition:str):

    weather_Data[city_name]={
        "date":date,
        "temperature": temperature,
        "humidity": humidity,
        "condition": weather_condition
    }


def query_by_city(city_name: str):
    if city_name in weather_Data:
        print("City:", city_name)
        print("Date:", weather_Data[city_name]["date"])
        print("Temperature:", weather_Data[city_name]["temperature"])
        print("Humidity:", weather_Data[city_name]["humidity"])
        print("Condition:", weather_Data[city_name]["condition"])
        print("-"*20)
    else:
        print("City not found.")

def update_weather_data(city_name: str, date: str, temperature: str, humidity: str, weather_condition: str):
    if city_name in weather_Data:
        weather_Data[city_name] = {
            "date": date,
            "temperature": temperature,
            "humidity": humidity,
            "condition": weather_condition
        }
        print("Updated.")
    else:
        print("City not found.")

def delete_weather_data(city_name: str):
    if city_name in weather_Data:
        del weather_Data[city_name]
        print("Deleted.")
    else:
        print("City not found.")


    
def is_valid_date(date: str):
    parts = date.split('/')
    if len(parts) != 3:
        return False
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not (1 <= int(month) <= 12):
        return False
    if not (1 <= int(day) <= 31):
        return False
    return True


while True:
    print('''
1. Add data
2. Query city
3. Update data
4. Delete data
5. Exit



''')
    choice = input("Choose an option: ")

    if choice == '1':
        city = input("Enter city name: ")
        date = input("Enter the data (e.g. 2026/01/07): ")
        while not is_valid_date(date):
            print("Invalid date format. Try again (YYYY/MM/DD)")
            date = input("Enter the date: ")
        temperature = input("Enter the temperature of that date: ")
        humidity = input("Enter the humidity of that data: ")
        weather_condition= input("Enter the weather condition of that date (e.g., sunny, rainy): ")
        input_weather_Data(city, date,temperature,humidity,weather_condition)

    elif choice == '2':
        city = input("Enter city name to query: ")
        query_by_city(city)

    elif choice == '3':
        city = input("Enter city name: ")
        date = input("Enter the date to update: ")
        while not is_valid_date(date):
            print("Invalid date format. Try again (YYYY/MM/DD)")
            date = input("Enter the date: ")
        temperature = input("New temperature: ")
        humidity = input("New humidity: ")
        condition = input("New condition: ")
        update_weather_data(city, date, temperature, humidity, condition)

    elif choice == '4':
        city = input("Enter city name: ")
        delete_weather_data(city)

    elif choice == '5':
        break
    else:
        print("Invalid choice.")

