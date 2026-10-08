import random
import string
from datetime import datetime
print("=== stromg password2")
file = open("passwords.txt", "a")
while True:
    while True:
        length=int(input("how long password win 10:  "))
        if length >= 10:
            break
        else:
            print("sory long must be 10")
            use_letters=input("letters")
            use_digits = input("use digits")
            use_symbols = input("symbols")
            characters=""
            if use_letters == "yes":
                characters += string.ascii_letters
            if use_digits == "yes":
                characters += string.digits
            if use_symbols == "yes":
                characters += string.punctuation
            if characters =="":
                print("you must shoose least one option")
                continue
    characters=""
    password ="".join(random.choice(characters)for i in range(length))
    print("your password is: ", password)
    time_now = datetime.now().strftime("%Y-%M-%d %H:%M")
    with open("password.txt","a") as file:
     file.write(f"{[time_now]} password: {password}\n")
     print("saved to passwords.txt")
    again = input("do you want another password: yes\no")
    if again != "yes":
       print("thanks for using strong password")
       file.close()
       break



                
        