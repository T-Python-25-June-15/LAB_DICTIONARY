phone_book = {
    "Amal"     : "0568323222" ,
    "Mohammed" : "0522222232" , 
    "Khadijah" : "0532335983" ,
    "Abdullah" : "0545341144" ,
    "Rawan"    : "0545534556" ,
    "Faisal"   : "0560664566" ,
    "Layla"    : "0567917077"
}

user_input = input("Enter the phone number: ")
digit_check = user_input.isdigit()

if len(user_input) != 10 or digit_check == False:
    print("This is invalid number")

else:
 number_found = False   
 for key , number in phone_book.items():
      if number == user_input:
        print(key)
        number_found = True
        break
         
 if number_found == False :
    print("Sorry, the number is not found")

         
   



    
