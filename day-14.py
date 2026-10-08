import random
secret_number = random.randint(1,10)
for i in range(3):
    guess=int(input("guess number from 1 to ten:"))
    if guess == secret_number:
      print("the number is true:",secret_number)
      break
    elif guess < secret_number:
      print("is less than",secret_number)
    else:
      print("is greater than",secret_number)
else:
  print("the time has expired")
