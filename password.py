import random
import string
from datetime import datetime
print("===strong password generator v2.0 ===")
file = open("passwords.txt", "a")
while True:
  while True:
      length = int(input("how long password? min 8: "))
      if length >= 8:
       break
  else:
    print("sory,length must be 8 or more")
    use_letters = input("letters: ")
    use_digits = input("use_digits: ")
    use_symbols = input("use_symbols: ")
    characters =""
    if use_letters =="yes":
       characters += string.ascii_letters
    if use_digits == "yes":
       characters += string.digits
    if use_symbols == "yes":
       characters += string.punctuation
    if characters =="": 
     print("you must choose at least one option")
    continue
  characters=string.ascii_letters+string.digits+string.punctuation
  password ="".join(random.choice(characters)for i in range(length))
  print("your password is",password) 
  time_now=datetime.now().strftime("%Y-%m-%d %H:%M") 
  with open("password.txt","a") as file:
   file.write(f"[{time_now}] password: {password}\n")
  print("saved to passwords.txt")
  again = input("do you want  another password yes/no: ")
  if again != "yes":
      print("thanks for using strong password")
      file.close() 
      break

