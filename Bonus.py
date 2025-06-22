weather_cities = {}


def add_city_weather(city_name: str) -> None:
    date = input('Enter date: ')
    temperature = input('Enter temperature: ')
    humidity = input('Enter humidity: ')
    weather_condition = input('Enter weather condition: ')

    weather_cities[city_name] = {
             'date': date,
             'temperature': temperature,
             'humidity': humidity,
             'weather_condition': weather_condition}
    
    
def display_city_weather(city_name: str) -> None:
    if city_name in weather_cities:
        print(f"City: {city_name}")
        print(f"Date: {weather_cities[city_name]['date']}")
        print(f"Temperature: {weather_cities[city_name]['temperature']}")
        print(f"Humidity: {weather_cities[city_name]['humidity']}")
        print(f"Weather Condition: {weather_cities[city_name]['weather_condition']}")

    else:
        print(f'Sorry this city: {city_name} not found it in data.')


def update_city_weather() -> None:
    print('The is a list of cities, which one you want to update?')
    cities = list_cities()
    user_input = int(input('Choose a number of city to update informations: '))
    city_update = cities[user_input - 1]
    print('Are you sure you want to update this city:')
    display_city_weather(city_update)
    user_want_update = input('write "yes" for continue to update this city {} information:'.format(city_update))
    if user_want_update == 'yes':
        add_city_weather(city_update)
        print(f'Update city: {city_update} is Done.')


def delete_city() -> None:
    print('This is a list of cities, wich one you want to delete?')
    cities = list_cities()
    user_input = int(input('Choose a number of city to delete it: '))
    city_delete = cities[user_input - 1]
    print('Are you sure you want to delete this city?:')
    display_city_weather(city_delete)
    user_want_delete = input(f"write 'yes' to delete this city: {city_delete} informations. ")
    if user_want_delete == 'yes':
        weather_cities.pop(city_delete)
        print(f'Delete city: {city_delete} is Done.')


# Helper funtions: 
def get_valid_city_name() -> str:
    city_name = input('Enter city name: ')
    while not city_name.replace(' ', '').isalpha():
        city_name = input('the name is invalid please enter valid name: ')
    return city_name


def list_cities() -> list:
    cities = list(weather_cities.keys())
    for i, city in enumerate(weather_cities, 1):
        print(f'{i}. {city}')
    return cities


print('---WELCOME TO WEATHER APP---')
menu = '''
1. to add new city weather
2. Display city weather
3. update city weather
4. delete city weather
5. write 'exit' to exit
'''


while True:
    print(menu)
    user_input = input('Choose a number or exit: ')

    if user_input == '1':
        city_name = get_valid_city_name()
        add_city_weather(city_name)

    elif user_input == '2':  
        city_name = get_valid_city_name()
        display_city_weather(city_name)

    elif user_input == '3':
        update_city_weather()

    elif user_input == '4':
        delete_city()

    elif user_input == 'exit':
        print('Goodbye')
        break
    else:
        print('Invalid input, please enter valid number or exit')