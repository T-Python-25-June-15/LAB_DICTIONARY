phone_numbers = {"Name" : "Number",
                 "0568323222" : "Amal",
                 "0522222232" : "Mohammed",
                 "0532335983" : "Khadijah",
                 "0545341144" : "Abdullah",
                 "0545534556" : "Rawan",
                 "0560664566" : "Faisal",
                 "0567917077" : "Layla",
                 "0590587255" : "Naif",}

user_input = input("Enter a phone number: ")

if not user_input.isdigit():
    print("This is invalid number")
elif len(user_input) != 10:
    print("This is invalid number")
elif user_input in phone_numbers:
    print(phone_numbers[user_input])
else:
    print("Sorry, the number is not found")