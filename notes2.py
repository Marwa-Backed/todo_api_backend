import random
import datetime 
while True:
   print("\n---Notes App") 
   print("1. add new  note")
   print("2. view all notes")
   print("3. Random note")
   print("4. delete note")
   print("5. Exit")
   print("6. Search note")
   print("7. Edit note")
   choice = input("choose a number of 1-7: ")
   if choice =="1":
      note = input("write your note:  ")
      with open ("notes.txt", "a", encoding="utf-8") as file:
         now = datetime.datetime.now()
         file.write(f"{now.strftime('%Y-%m-%d %H:%M'  )}-{note}\n")
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
            print("no notes file found")
   if choice =="3":
      try:
         with open ("notes.txt","r", encoding="utf-8")as file:
          notes = file.readlines()
         if len(notes)==0:
            print("No notes to choose from")
         else:
          random_note =random.choice(notes)
         print(f"Random note for you: {random_note.strip()}")
      except FileNotFoundError:
                print("no notes file found")
   elif choice == "4":
      try:
         with open("notes.txt","r", encoding="utf-8")as file:
            notes = file.readlines()
            if len(notes)==0:
             print("No notes to delete")
            else:
              for i, n in enumerate(notes):
               print(f"{i+1}.{n.strip()}")
            num=int(input("Enter note number to delete"))
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
   elif choice == "6":
      keyword = input("enter keyword: ")
      try:
            with open("notes.txt", "r",encoding="utf-8") as file:
             notes=file.readlines()
            found=False
            print("\n search result")
            for i,n in enumerate(notes):
               if keyword.lower() in n.lower():
                  print(f"{i+1}.{n.strip()}")
                  found=True
                  if not found:
                     print("not found")
      except FileNotFoundError:
                   print(" no notes file found")
                   break
   elif choice == "7":
      try:
         with open("notes.txt", "r",encoding="utf-8") as file:
            notes=file.readlines()
            if len(notes)==0:
               print("No notes to edit")
            else:
               print("choose a number to edit:  ")
               for i, n in enumerate(notes):
                  print(f"{i+1}.{n.strip()}")
                  num =int(input("enter note number to edit"))
                  if 1 <= num <= len(notes):
                     print(f"old note:{notes[num-1].strip()}")
                     new_note=input("write new note:  ")
                     notes[num-1] = new_note+"\n"
                     with open("notes.txt","w" ,encoding="utf-8") as file:
                        file.writelines(notes)
                        print("edited successfully")
                     break
               else:
                   print("Invalid number")
      except FileNotFoundError:
         print("no notes file found")
      except ValueError:
       print("Please enter a valid number")
       break
else:
       print("Invalid, choose 1,2,3,4,5,6,7")
   
           

      
            


   
     


        
     

