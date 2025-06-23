phone_book:dict = { 
"0568323222": "Amal",
"0522222232": "Mohammed",
"0532335983": "Khadijah",
"0545341144": "Abdullah",
"0545534556": "Rawan",
"0560664566": "Faisal",
"0567917077": "Layla"
}

def get_valid_input(prompt, phone_number):
    while True:
        try:
            int(phone_number)
            for element in phone_number:
                if int(element) not in range(0, 10):
                    print("This is invalid number.")
                    phone_number:str = input("Please enter a phone number to see the name of the owner: ")
                elif len(phone_number) > 10 or len(phone_number) < 10:
                    print("This is invalid number.")
                    phone_number:str = input("Please enter a phone number to see the name of the owner: ")    
                else:
                    return phone_number
        except ValueError:
            print("This is invalid number.")
            phone_number:str = input("Please enter a phone number to see the name of the owner: ")

print("Welcome to the phone book System")
while True:
    print("Phone book Menu:")
    print("1. View the name of the phone owner")
    print("2. exit")
    choice = input("Enter your choice: ",)

    if choice == "1":
        phone_number:str = input("Please enter a phone number to see the name of the owner: ")
        phone_number:str = get_valid_input("Please enter a phone number to see the name of the owner: ", phone_number)
        if phone_number in phone_book:
            print(f"The name of the owner is: {phone_book.get(phone_number)}")  
        elif phone_number not in phone_book:
            print("Sorry, the number is not found")  
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")


