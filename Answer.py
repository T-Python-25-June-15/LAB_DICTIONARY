Book_program = {"Amal":"0568323222", "Mohammed":"0522222232", "Khadijah":"0532335983", "Abdullah":"0545341144", "Rawan":"0545534556", "Faisal":"0560664566", "Layla":"0567917077"}
Phone_number = input("Please provide the phone number: ")

def Book_program_checking(Phone_number):
    is_it_valid(Phone_number)
    number_found = False
    for key, value in Book_program.items():
        if value in Phone_number:
            number_found = True
            print(key)
    if number_found == False:
        print("Sorry, the number is not found")


def is_it_valid(Phone_number):
    while len(Phone_number) < 10 or len(Phone_number) > 10 or not Phone_number.isdigit():
        print("This is invalid number") 
        Phone_number = input("Please provide the phone number: ")

Book_program_checking(Phone_number)