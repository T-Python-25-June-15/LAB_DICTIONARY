#Luluh Almogbil 
'''
# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".



'''
print("Welcome to my phone book program")
mynumbers = {"0568323222":"Amal",
             "0522222232":"Mohammed",
             "0532335983":"Khadijah",
             "0545341144":"Abdullah",
             "0545534556":"Rawan",
             "0560664566":"Faisal",
             "0567917077":"Layla "
             }

#print(mynumbers)
check = input("Please provide a number so i can check the owner: ")


while not (len(check) == 10 and check.isdigit()):
    print("This is invalid number")
    check = input("Please enter a valid number and make sure it is only 10 digits: ")

if check in mynumbers:
     print(f"The {check} number is found!")
     print(f"The owner is {mynumbers[check]} ")
else:
     print("Sorry, the number is not found")
     


        
    




