phone_number_dictionary= {"0500128005" : "Abdulaziz",
                          "0522222232" : "Mohammed",
                          "0532335983" : "Khadijah",
                          "0545341144" : "Abdullah",
                          "0545534556" : "Rawan",
                          "0560664566" : "Faisal",
                          "0567917077" : "Layla"
                          }


def is_number_invalid(phone_number:str):
    if len(phone_number) != 10: 
        print("This is invalid number, is is less or more than 10 numbers")
    elif not phone_number.startswith("05"):
        print("This is invalid number, is does not start whith 05*****")
    elif not phone_number.isdigit():
        print("This is invalid number, the number shoude be only numbers")
    else: return True


def find_the_owner(phone_number:int):
    if phone_number_dictionary.get(phone_number) != None:
        return phone_number_dictionary.get(phone_number)
    else:
        print("this phone number is not in our dictionary")


while True:
    user_number=input("Enter the phone number to know the name of owner: ")

    if is_number_invalid(user_number):
        owner_name=find_the_owner(user_number)
        print(f"The onewr of {user_number} is {owner_name}")
    





