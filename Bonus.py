# Bonus lab (wasan alqahtani)

#intiat empty dictionary
weather_data={}
def initalized_dictionary():
    '''this method takes input from user and then added to the dictionary'''
    flag = True
    while flag:
        cityname = input("please enter city name: ")
        date = input("please enter city date: ")
        temperature = input("please enter city temperature: ")
        humidity = input("please enter city humidity: ")
        weather_condition = input("please enter weather condition eg (rainy / sunny): ")
        #validate the input and then added to the dictionary
        if cityname.isdigit()== False and date.isdigit() ==False and temperature.isdigit() and humidity.isdigit() and weather_condition.isdigit()== False:
            weather_data[cityname] = {"date":date, "temperature":temperature, "humidity":humidity, "condition":weather_condition}
            flag = False
            print("added sucessfully")
        else:
                print("wrong entry type try again")

      
def display_info(cityname):
    '''this method takes the city name as an argument and then display all information'''
    #check if the city name exist or not
    if check_available(cityname):
        #display the information
        print(f"All Information of {cityname} are :")
        print(f"date: {weather_data[cityname]["date"]}")
        print(f"temperature: {weather_data[cityname]["temperature"]}")
        print(f"humidity: {weather_data[cityname]["humidity"]}")
        print(f"weather condition: {weather_data[cityname]["condition"]}")
    else :
        print("this city is'nt in the dictionary")

def check_available(cityname):
    '''this method take the city name as an argument and then return true or false
    to check if it in the dictionary or not'''
    return cityname in weather_data 


def update_info(cityname):
    '''this method take the city name as an argument and then update information
    based on what user want'''
    #check if the city name in the dictionary or not 
    if check_available(cityname):
        print("What you want to update :")
        print("1. City name ")
        print("2. Date")
        print("3. temperature")
        print("4. humidity")
        print("5. weather condition")
        thechoice= input("please choose an option that you want to update: ")
        #update information based on user 
        match thechoice:
            case "1":
                new_cityname = input("please enter city name: ")
                weather_data[new_cityname]=weather_data.pop(cityname)
            case "2":
                 new_date = input("please enter city date: ")
                 weather_data[cityname].update({"date":new_date})
                 
            case "3":
              new_temperature = input("please enter city temperature: ")
              weather_data[cityname].update({"temperature":new_temperature})

            case "4":
                newhumidity = input("please enter city humidity: ")
                weather_data[cityname].update({"humidity":newhumidity}) 

            case "5":
                newweather_condition = input("please enter weather condition eg (rainy / sunny): ")
                weather_data[cityname].update({"condition":newweather_condition})

    else :
        ("there is no information with this city name")

def delete_info(cityname):
    '''this method take cityname as an argument and then delete the information 
    of this city'''
    #check if the city name in the dictionary or not
    if check_available(cityname):
        #delete
        weather_data.pop(cityname)
        print("delete done succssfully")
    else:
        ("there is no information with this city name")

#print menue
while True:
    print("\nWeather Data Aggregation Menue")
    print("-"*20)
    print("1. Store Wether data in dictionary")
    print("2. Query by City(display all information based on city name)")
    print("3. Update or delete weather information")
    print("4. Exit")
    option = input("please choose number from menue above: " )

    match option:
        case "1":
            print("-"*20)
            initalized_dictionary()
            print("-"*20)
        case "2":
            print("-"*20)
            cityname = input("please enter city name: ")
            display_info(cityname)
            print("-"*20)

        case "3":
            print("-"*20)
            option2 = input("please press 1 to update or 2 to delete: ")
            if option2 == "1" :
                cityname = input("please enter city name: ") 
                update_info(cityname)
                print("-"*20)
            elif option2 =="2":
                cityname = input("please enter city name: ") 
                delete_info(cityname)
            else:
                print("wrong number try again")
        case "4":
            break
        case _:
            print("wrong number please try again")





