phone_book = {
    "name": ["Amal", "Mohammed", "Khadijah", "Abdullah", "Rawan", "Faisal", "Layla"],
    "phone": ["0568323222", "0522222232", "0532335983", "0545341144", "0545534556", "0560664566", "0567917077"]
}

user_input = input('Enter phone number: ')
if (user_input.isdigit()) and (len(user_input) == 10):
    if user_input in phone_book['phone']:
        phone_index = phone_book.get('phone').index(user_input)
        name = phone_book.get('name')[phone_index]
        print(f'this phone {user_input}, Owner by {name}')
    else: 
        print('Sorry, the number is not found.')
else: 
    print('This is invalid number')