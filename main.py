


phone_book = {"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah"
               ,"0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}

def isNumExist(number:str):
    return number in phone_book.keys()

def isNumValid(number:str):
    return len(number) == 10 and number.isdigit() # isdigit() returns True if all characters are digits.
        

print("---- WELCOME TO PHONE BOOK PROGRAM ----")
number = input("Enter the number: ")

if isNumValid(number):
    if isNumExist(number):        
        print("The owner is:",phone_book.pop(number))


    else:
        print("Sorry, the number is not found")

else:
    print("This is invalid number")





















