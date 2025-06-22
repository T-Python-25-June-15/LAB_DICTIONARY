
phone_number_set = [
    {
        "name": "Amal",
        "phone": 966568323222
    },
    {
        "name": "Mohamed",
        "phone": 966522222232
    },
    {
        "name": "Khadijah",
        "phone": 966532335983
    },
    {
        "name": "Abdullahal",
        "phone": 966545341144
    },
    {
        "name": "Rawan",
        "phone": 966545534556
    },
    {
        "name": "Faisal",
        "phone": 966560664566
    },
    {
        "name": "Layla",
        "phone": 966567917077
    }
]

def findUserNumber(number:int) -> dict:
    '''
        find the phone number from a list that contains a dict
        
        Args:
            int: number
            
        Return:
            dict or if not founded return None
    '''
    for i in phone_number_set:
        if i["phone"] == number:
            return i
        
    return None 

def main():
    user_phone = input("your phone number: (05........): ")
    if len(user_phone) != 10: 
        print("This is invalid number")
        return
    if user_phone.isalpha():
        print("This is invalid number")
        return
    
    user_phone = user_phone[1:] # remove 0
    user_phone = "966" + user_phone # add 966
    user_phone = int(user_phone) # conver to integer
    if findUserNumber(user_phone) != None:
        print(findUserNumber(user_phone)["name"])
    else:
        print("Sorry, the number is not found")


main()