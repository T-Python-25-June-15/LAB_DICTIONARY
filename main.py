phone_book=[
    {"name":"Amal",
    "number":"0568323222"},
    {"name":"Mohammed",
    "number":"0522222232"},
    {"name":"Khadijah",
     "number":"0532335983"},
     {"name": "Abdullah",
      "number":"0545341144"},
      {"name":"Rawan",
       "number":"0545534556"},
       {"name": "Faisal",
        "number":"0560664566"},
        {"name":"Layla",
         "number":"0567917077"}]
n=input("input your number ")
def find_number(n):
   
    for person in phone_book:
         if person["number"] == n:
             print(f"the number for {person['name']} ")
             return
    else:
        print("Sorry, the number is not found")

def vaild_num(n):

    if len(n)!=10 or not n.isdigit():
        print("This is invalid number")
        return False
    return True
if vaild_num(n):
   find_number(n)
