#Phone Book Program
user_condition:bool = True
numbers_dictionary = {"0568323222":"Amal",
                      "0522222232":"Mohammed",
                      "0532335983":"Khadijah",
                      "0545341144":"Abdullah",
                      "0545534556":"Rawan",
                      "0560664566":"Faisal",
                      "0567917077":"Layla"}

while user_condition:
    user_input:str = input("Please enter phone number to provide the name or type 'exit' to quit: ")
    if user_input.lower() == "exit":
        user_condition = False
    #check if the user enter proper number
    elif user_input.isnumeric() and len(user_input) == 10:
        #print the name for the number or apologize if it is not there 
        print(f"{numbers_dictionary.get(user_input,'Sorry, the number is not found')}")   
    elif (user_input.isnumeric() and len(user_input) != 10) or (user_input.isnumeric() == False):
        print("This is invalid number")    
print("Thank you for using the Phone Book Program")