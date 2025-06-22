
cities = {}

print('welcome to Weather Data Aggregation system\n')


message = '''
1.add new city
2.Query by city
write exit to leave
'''

msg = input(message)

while msg != 'exit':
    if msg == '1':
        city = input('write city name: ')
        date = input('write city date: ')
        temperature = input('write city temperature: ')
        while(temperature.isdigit() == False):
            print("please enter valid temperature")
            temperature = input('write city temperature: ')

        humidity = input('write city humidity: ')
        weather_condition = input('write city weather condition: ')
        cities[city] = {
            'date': date,
            'temperature': temperature,
            'humidity': humidity,
            'weather_condition': weather_condition
        }
        print("city added successfully")
        
    elif msg == '2':
        city_name = input('write city name: ')
        if city_name in cities:
            print("city name:", city_name)
            print("city date:", cities[city_name]['date'])
            print("city temperature:", cities[city_name]['temperature'])
            print("city humidity:", cities[city_name]['humidity'])
            print("city weather condition:", cities[city_name]['weather_condition'])
        else:
            print("city not found")
    else:
        print("invalid option")
    
    msg = input(message)
