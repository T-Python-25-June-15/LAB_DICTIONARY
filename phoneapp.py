dictionary = {"0568323222":"Amal",
              "0522222232":"Mohammed",
              "0532335983":"Khadijah",
              "0545341144":"Abdullah",
              "0545534556":"Rawan",
              "0560664566":"Faisal",
              "0567917077":"Layla"}


while True:
    enternumber = input("Give me the number: ")

    theNumberLength = len(enternumber)
    
    if enternumber.isdigit():
        if theNumberLength == 10:
            if enternumber in dictionary:
                print(dictionary[enternumber])
            else:
                print("Sorry, the number is not found")
        else:
            print("This is invalid number")
    else:
        print("This is invalid number")
        

