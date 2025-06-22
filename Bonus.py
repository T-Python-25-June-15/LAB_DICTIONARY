# Exercise: Weather Data Aggregation
# Objective: Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

# Requirements:
# Input Weather Data: Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
# Store Data in a Dictionary: Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
# Query by City: Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.
# Guidelines:
# Use nested dictionaries to store the weather data efficiently.
# Implement separate functions for inputting data, querying by city.
# Validate user inputs to ensure correctness.
# Challenge:
# Extend the program to allow the user to update or delete weather data for a specific city and date.


weather_data = {}

def add_city():
    city_name = input("Enter city name: ")
    date = input("Enter date: ")
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter weather condition: ")

    city_info = {
        "date": date,
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    weather_data[city_name] = city_info
    print(f"{city_name} added.\n")


def search_city():
    city_name = input("Enter name of city to search: ")
    if city_name in weather_data:
        print(f"{city_name}: {weather_data[city_name]}\n")
    else:
        print("City not found.\n")


def display_cities():
    if not weather_data:
        print("No cities added yet.\n")
    else:
        for key, value in weather_data.items():
            print("City: " + str(key) + "\nData: " + str(value) + "\n")

def update_city():
    city_name = input("Enter name of city to update: ")
    if city_name in weather_data:
        print(f"Current data: {weather_data[city_name]}")
        date = input("Enter new date: ")
        temperature = input("Enter new temperature: ")
        humidity = input("Enter new humidity: ")
        condition = input("Enter new weather condition: ")

        weather_data[city_name] = {
            "date": date,
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }
        print(f"{city_name} updated.\n")
    else:
        print("City not found.\n")


def delete_city():
    city_name = input("Enter name of city to delete: ")
    if city_name in weather_data:
        del weather_data[city_name]
        print(f"{city_name} deleted.\n")
    else:
        print("City not found.\n")


while True:
    print("\n1. Add new city")
    print("2. Search city")
    print("3. Display all cities")
    print("4. Update city")
    print("5. Delete city")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_city()
    elif choice == "2":
        search_city()
    elif choice == "3":
        display_cities()
    elif choice == "4":
        update_city()
    elif choice == "5":
        delete_city()
    elif choice == "6":
        break
    else:
        print("Invalid choice.\n")