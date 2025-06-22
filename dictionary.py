number_book={"Amal": "0568323222", "Mohammed":"0522222232", "Khadijah":"0532335983", "Abdullah":"0545341144", "Rawan":"0545534556", "Faisal":"0560664566", "Layla":"0567917077"}

number = input("Enter the number: ")

if len(number) != 10 or not number.isdigit():
    print("This is invalid number")
else:
    found = False

    for name in number_book:
        if number_book[name] == number:
            print(name)
            found = True

    if found == False:
        print("not found")

    



