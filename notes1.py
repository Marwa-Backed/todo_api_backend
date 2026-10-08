import random
while True:
    print("\n---Notes App") 
    print("1. add new app")
    print("2. view all notes")
    print("3. Random note")
    print("4. Exit")
    choice = input("choose a number of 1-4:  ")
    if choice =="1":
     note = input("write your note")
     with open ("notes.txt", "a", encoding="utf-8") as file:
         file.write(note+ "\n")
         print("saved successfully")
    elif choice =="2":
     with open("notes.txt","r", encoding="utf-8") as file:
      notes = file.readlines()
      if len(notes)==0:
         print("No notes yet")
      else:
         print("\n ---Your notes---")
         for i, n in enumerate("notes.1"):
            print(f"{i}.{n.strp()}")
            print("No notes Yet. Add noe first")
    elif choice == "4":
     print("Thanks for using Notes APP")
    break
else:
         print("Invalid. Choose 1,2,3 or 4")
           

      
            


   
     


        
     

