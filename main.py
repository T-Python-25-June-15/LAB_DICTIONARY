
list = {
        "Amal":"0568323222", 
        "Mohammed":"0522222232",
        "Khadijah":"0532335983",
        "Abdullah":"0545341144",
        "Rawan":"0545534556", 
        "Faisal":"0560664566",
        "Layla":"0567917077"
}
user_choise= input("enter phone number\n")
if len(user_choise) < 10:
    print("This is invalid number")

elif user_choise.isdigit() == False:
    print("This is invalid number")

username = None

for name, Number in list.items():
    if user_choise == Number:
        username = name
        break

if username:
    print(f"name is {username}")
else:
    print("Sorry, the number is not found")