weather_data = {}

def add_weather():
    city = input("enter city: ")
    date = input("enter date : ")
    temp = input("enter temperature: ")
    humidity = input("enter humidity: ")
    condition = input("enter condition: ")

    if city not in weather_data:
        weather_data[city] = {}

    if temp.isdigit() and humidity.isdigit():
        weather_data[city][date] = {

            "temperature": temp,
            "humidity": humidity,
            "condition": condition
    }
        print("data added")
    else:
        print("invalid")



def show_city():
    city = input("enter city: ")
    if city in weather_data:
        print("weather data for", city)
        for date in weather_data[city]:
            print("Date:", date)
            print("Temperature:", weather_data[city][date]["temperature"])
            print("Humidity:", weather_data[city][date]["humidity"])
            print("Condition:", weather_data[city][date]["condition"])
            print()
    else:
        print("city not found")

while True:
    print("1- add data")
    print("2- show city")
    print("3- exit")

    choice = input("choose: ")

    if choice == "1":
        add_weather()
    elif choice == "2":
        show_city()
    elif choice == "3":
        break
