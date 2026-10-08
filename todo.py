import os
from datetime import datetime
from colorama import  Fore, Style, init
init(autoreset=True)
FILE_NAME="tasks.txt"
def load_tasks():
        if not os.path.exists(FILE_NAME):
          return[]
        with open(FILE_NAME, "r", encoding="utf-8")as file:   
          return[line.strip()for line in file if line.strip()]
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
def get_color(priority):
    if priority=="High":return Fore.RED
    if priority=="Medium":
        return Fore.YELLOW
        return Fore.GREEN
def is_overdue(d_str):
    if d_str == "no date":
          return False
          task_date=datetime.datetime.strptime(d_str, "%Y-%m-%d").date()
          return task_date < datetime.date.today()
while True: 
    print("\n---To-Do List---")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Delete all completed")
    print("6. Edit Task")
    print("7. Search Task")
    print("8. Statistics")
    print("9. Exit")
    choice=input("choose 1-9:  ")
    if choice == "1":
        print("Type Done To go Back")
        while True:
            task=input("write your task : ")
            if task.lower()=="done":
                break
            if task.strip()=="":
                continue
            priority=input("priority[High/Medium/Low]: ").strip().capitalize()
            if priority not in ["High","Medium","Low"]:priority="Low" 
            category=input("Category[Work/Study/Personal]: ").strip().capitalize()
            if category not in ["Work", "Study", "Personal"]:
              category="Personal"
            date_input=input("Due date(YYYY-MM-DD) or leave empty: ").strip()
            if date_input == "":
              date_input ="no date"
            with open(FILE_NAME, "a", encoding="utf-8") as file:
             file.write(f"0 - {task} - {priority} - {category} - {date_input}\n")
             print("task added successfully")
             continue
    elif choice == "2":
            tasks=load_tasks()
            if not tasks:
             print("No tasks yet")
             continue
            else:
                print("--Your tasks--")
            for idx, task in enumerate(tasks,1):
                task_strip = task.strip()
                if task_strip == "" or " - " not in task_strip:
                    continue
                parts=task.split(" - ", 4)
                if len(parts)== 5:
                    status,text,pri,cat,d=parts
                    check="[x]"if status== "1" else "[ ]"
                    color= get_color(pri)
                    overdue = ""
                    if d != "no date" and is_overdue(d) and status=="0":
                        overdue=f"{Fore.RED} overdue! {Style.RESET_ALL}"
                    print(f"{idx}. {color}  {check}  {text}  {Style.RESET_ALL}  {d}{overdue}")
                else:
                    print("waring skipping invalid task") 
                    continue
    elif choice == "3":
            tasks=load_tasks()
            if not tasks:
              print("No task yet")
              continue         
            print("--Your tasks--")
            for idx, task in enumerate(tasks, 1):
                task_strip = task.strip()
                if task_strip == "" or " - " not in task_strip:
                 continue
                parts = task.split(" - ", 4)
                if len(parts) == 5:
                    status, text, pri, cat, d = parts
                    check="[x]" if status=="1" else"[ ]"
                    color = get_color(pri)
                    overdue=""
                    if d != "no date" and is_overdue(d) and status == "0":
                      overdue=f"{Fore.RED}OVERDUE!{Style.RESET_ALL}"
                    print(f"{idx}. {color}  {check}  {text} - {d}{overdue}  {Style.RESET_ALL}") 
                else:
                    print(f"{idx}. {task}")
                    print("0. Back To Home")
            num=int(input("Which task number is done?  or press 0 to cancel  "))
            if num ==0:
                 print("Cancelled")
                 continue
            if 1 <= num <= len(tasks):
                p=tasks[num- 1].split(" - ", 4)
                if len(p) == 5:
                 if p[0]=="0":
                    tasks[num-1]= f"1 - {p[1]} - {p[2]} - {p[3]} - {p[4]}"
                    save_tasks(tasks)
                    print("marked as done")
            else:
             print("task already done")
             continue
    elif choice == "4":
            tasks = load_tasks()
            if not tasks:
             print("No tasks Yet")
             continue
            else:
                print("--Your tasks--")
                for idx,task in enumerate(tasks, 1):
                    task_strip = task.strip()
                    if task_strip == "" or " - " not in task_strip: 
                      continue
                    parts=task.split(" - ", 4)
                    if len(parts) == 5:
                        status,text, pri, cat, d= parts
                        check = "[x]" if status=="1" else"[ ]"
                        color = get_color(pri)
                        overdue=""
                        if d != "no date" and is_overdue(d) and status=="0":
                          overdue=f"{Fore.RED}OVERDUE!{Style.RESET_ALL}"
                        print(f"{idx}. {color}  {check}  {text} - {d}{overdue} {Style.RESET_ALL} ") 
                    else:
                        print("f{idx}. {task}")
                num=int(input("Enter task number to delete?  or press 0 Back To Home")) 
                if num == 0:
                    print("cancelled")
                    continue
                if 1 <=num<=len(tasks):
                    deleted= tasks.pop(num-1)
                    save_tasks(tasks)
                    print("task deleted")
                else:
                    print("Invalid number")
                    continue
    elif choice == "5":
        tasks=load_tasks()
        if not tasks:
            print("No tasks yet")
            continue
        original_count = len(tasks)
        tasks=[task for task in tasks if not task.strip().startswith("1 -")]
        deleted_count= original_count - len(tasks)
        save_tasks(tasks)
        print(f"deleted {deleted_count} completed tasks")
        continue
    elif choice == "6":
        tasks = load_tasks()
        if not tasks:
            print("No tasks Yet")
            continue
        print("-- your tasks---")
        for idx, task in enumerate(tasks, 1):
            task_strip=task.strip()
            if task_strip == "" or " - " not in task_strip:
                continue
            parts=task.split(" - ", 4)
            if len(parts)== 5:
                status,text, pri, cat, d = parts
                check="[x]" if status == "1" else "[ ]"
                color = get_color(pri)
                overdue = ""
                if d != "no date" and is_overdue(d) and status=="0":
                    overdue= f"{Fore.RED} OVERDUE!{Style.RESET_ALL}"
                print(f"{idx}. {color}  {check}  {text} - {d}{overdue} {Style.RESET_ALL}")
            else:
                print(f"{idx}. {task}")
        num=int(input("which task number to Edit?  or press 0 to cancel "))
        if num == 0:
            continue
        if 1 <= num <= len(tasks):
            new_text = input("Enter New Text ")
            p=tasks[num-1].split(" - ", 4)
            if len(p)==5:
                tasks[num-1]= f"{p[0]} - {new_text} - {p[2]} - {p[3]} - {p[4]}"
            else:
                tasks[num-1]= f"0 - {new_text} - low - personal - no date"
            save_tasks(tasks)
            print("Task Updated")
        else:
            print("Please Enter a number")
    elif choice == "7":
        keyword=input("Enter Keyword to search: ").lower()
        task=load_tasks()
        found=[task for task in tasks if keyword in task.lower()]
        print(f"-- fount{len(found)} tasks --")
        for task in found: print(task.split(" - ", 4) [1])
        continue
    elif choice == "8":
        task = load_tasks()
        total = len(tasks)
        completed = len([task for task in tasks if task.startswith("1 -")])
        print("\n -- Statistics--")
        print(f"total: {total}, completed: {completed}, Remaining: {total-completed}")
        if total >0: print(f"Progress:{(completed/total)*100:.1f}%")
        continue
    elif choice == "9":
        print("Goodbye!")
        break
                
            
        
       
        
                   
                   


