import random
options =["rock","paper","scissors"]
computer =random.choice(options)
guess=input("rock, paper,or scissors: ")
if  guess=="rock":
    print("you win! Rock smashes ", computer)
elif guess == "paper": 
   print("you win! packages of :", computer) 
else:
    print ("you are out the game")



