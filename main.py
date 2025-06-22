# Dictionary contain numbers as keys and names as values
numbers_dic={

    "0568323222":"Amal", 
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"

}
# Ask the user to input a number
num=input("Enter your number:")

# cheak if the input validate 
if len(num) != 10 or num.isdigit == False:
    print("This is invalid number.")
else:
    if num in numbers_dic.keys():
       print("the number is found")
       print("The owner is: ",numbers_dic[num])
    else:
        print("Sorry, the number is not found")






