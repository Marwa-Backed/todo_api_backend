import random
secret_number=random.randint(1,10)
guess=int(input("guess number from 1 to ten:"))
if guess == secret_number:
    print("the number is true:",secret_number)
