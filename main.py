

phone_book = {"Amal":"0568323222","Mohammed":"0522222232","Khadijah":"0532335983","Abdullah":"0545341144"
              ,"Rawan":"0545534556","Faisal":"0560664566","Layla":"0567917077"}

def isNumExist(number:str):
    return number in phone_book.values()

def isNumValid(number:str):
    return len(number) == 10 and number.isdigit() # isdigit() returns True if all characters are digits.
        

print("---- WELCOME TO PHONE BOOK PROGRAM ----")
number = input("Enter the number: ")

if isNumValid(number):
    if isNumExist(number):        
        for name, num in phone_book.items():
            if num == number:
                print("The owner is:",name)
                break

    else:
        print("Sorry, the number is not found")

else:
    print("This is invalid number")





















