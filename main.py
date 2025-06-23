print()
print("-" * 16)
print("Contacts Program")
print("-" * 16)

print()
print()

number = input("Enter a number: ")


contacts = { "0568323222" : "Amal",
             "0522222232" : "Mohammed",
             "0532335983" : "Khadijah",
             "0545341144" : "Abdullah",
             "0545534556" : "Rawan",
             "0560664566" : "Faisal",
             "0567917077" : "Layla"
             }

if not number.isdigit():
    print("Symbols or letters not accepted.")
elif number in contacts:
    print(f"The owner of the number {number} is {contacts[number]}.")
elif len(number) != 10:
    print("This is invalid number, it must contain only 10 numbers.")
else:
    print("Sorry, the number is not found.")
