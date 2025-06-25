weather_data = {}

while True:
    print("\n🌦️ MENU:")
    print("1. Add")
    print("2. Show")
    print("3. Delete")
    print("4. Update")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        city = input("City name: ").title()
        temp = input("Temperature (°C): ")
        condition = input("Weather condition (Sunny / Rainy / Cloudy): ").title()

        weather_data[city] = {
            "temperature": temp,
            "condition": condition
        }
        print("✅ Weather data added.")

    elif choice == "2":
        city = input("Enter city name to view: ").title()
        if city in weather_data:
            data = weather_data[city]
            print(f"\n📍 {city}")
            print(f"🌡️ Temperature: {data['temperature']}°C")
            print(f"🌤️ Condition: {data['condition']}")
        else:
            print("No data for this city.")

    elif choice == "3":
        city = input("Enter city name to delete: ").title()
        if city in weather_data:
            del weather_data[city]
            print("✅ City deleted.")
        else:
            print(" No data for this city.")

    elif choice == "4":
        city = input("Enter city name to update: ").title()
        if city in weather_data:
            new_temp = input("Enter new temperature (°C): ")
            new_condition = input("Enter new weather condition (Sunny / Rainy / Cloudy): ").title()

            weather_data[city] = {
                "temperature": new_temp,
                "condition": new_condition
            }
            print("✅ Data updated.")
        else:
            print(" No data for this city.")

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print(" Invalid option. Try again.")
