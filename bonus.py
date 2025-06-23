print("Welcome to the Weather Data System")
weather_data:dict= {}

def get_valid_input(prompt, value):
    pass


def inputting_data():
    city_name = input("Enter the city name: ")
    date = input("Enter the date YYYY-MM-DD: ")
    temperature = input("Enter the temperature: ")
    humidity = input("Enter the humidity: ")
    weather_condition = input("Enter the weather condition: ")

    if city_name not in weather_data:
        weather_data[city_name] = {}
        
    weather_data[city_name] = {
        "city name": city_name,
        "date": date, 
        "temperature": temperature, 
        "humidity": humidity,
        "weather_condition": weather_condition}
    
def querying():
    city_name = input("Enter the city name: ")
    if city_name in weather_data:
        for city_name in weather_data:
            print(f"{weather_data[city_name]}")
    else:
        print("City not found.")

def update_data():
    pass

def delete_data():
    pass

while True:
    print("Weather Data System Menu:")
    print("1. Input Weather Data")
    print("2. Query by City")
    print("3. exit")
    choice = input("Enter your choice: ",)
    if choice == "1":
        inputting_data()
    elif choice == "2":
        querying()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")



