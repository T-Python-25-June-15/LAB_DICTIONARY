#lab dictionary (wasan alqahtani)

#create dictionary
phones_dictorany={
    '0568323222':"Amal", 
    '0522222232':'Mohammed',
    '0532335983':'Khadijah', 
    '0545341144':'Abdullah',
    '0545534556':'Rawan',
    '0560664566':'Faisal',
    '0567917077':'Layla'}

#take a phone number from the user 
phone_number=input("please provide the phone number: ")

#check if the number is not less than or greater than 10 and doesnt conatins letters and symbols 
if len(phone_number)!=10 or  phone_number.isdigit() == False  :
    print("invalid phone number")

else:
#check if the number is exists or not 
    if phone_number in phones_dictorany:
       print(f"The owner of this phone is : {phones_dictorany[phone_number]}") 
    else : 
        print("the phone number is'nt exist")
