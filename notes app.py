import random
while True:
    print("\n---Notes App") 
    print("1. add new app")
    print("2. view all notes")
    print("3. Random note")
    print("4. delete note")
    print("5. Exit")
    choice = input("choose a number of 1-5: ")
    if choice =="1":
     note = input("write your note")
     with open ("notes.txt", "a", encoding="utf-8") as file:
         file.write(note + "\n")
         print("saved successfully")
    elif choice =="2":
      try:
         with open("notes.txt","r", encoding="utf-8") as file:
          notes = file.readlines()
         if len(notes)==0:
           print("No notes yet")
         else:
           print("\n ---Your notes---")
           for i, n in enumerate(notes):
              print(f"{i+1}.{n.strip()}") 
      except FileNotFoundError:
       if choice =="3":
            try:
               with open ("notes.txt","r", encoding="utf-8")as file:
                  notes = file.readline()
                  if len(notes)==0:
                     print("No notes to choose from")
                  else:
                     random_note =random.choice(notes)
                     print(f"Random note foe you: {random_note.strip()}")
            except FileNotFoundError:
             print("no notes file found")
       elif choice == "4":
            with open ("notes.txt","r", encoding="utf-8")as file:
                  notes = file.readline()
                  if len(notes)==0:
                     print("No notes to delete")
                  else:
                     for i, n in enumerate(notes):
                        print(f"{i+1}.{n.strip()}")
                  num = int(input("Enter note number to deleted"))
                  if 1 <= num <= len(notes):
                   deleted_note = notes.pop(num-1)
            with open("notes.txt", "w", encoding="utf-8") as file:
              file.writelines(notes)
              print(f"Deleted: {deleted_note.strip()}")
       else:
         print("Invalid number:")
      except FileNotFoundError:
         print("no notes file found")
      except ValueError:
         print("please enter a valid number")
    elif choice == "5":
         print("Thanks for using Notes APP")
    break
else:
         print("Invalid. Choose 1,2,3 or 4")
           

      
            


   
     


        
     

