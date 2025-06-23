phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number = input ("Enter the phone number:")
if number.isdigit():
    if len (number) == 10:
        if number in phone_book:
            print ("The owner is ", phone_book[number])
        else:
            print ("sorry, The number is not found")
    else:
         print ("This invalid number")
else:
         print ("This is invalid number")
