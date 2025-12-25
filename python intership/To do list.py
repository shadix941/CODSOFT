def to_do_list():
    task=[] # list to store task
    
    while True:           #menu
        print("\n To-Do-LIST MENU:")
        print("1.View task")
        print("2.Add task")
        print("3.Remove task")
        print("4.clear all task")
        print("5.Exit")

        choice =input("Choose a option:").strip()
        
        if choice =="1":  #View task
             if task:
                  print("your tasks:")
                  for i,t in enumerate(task,1):
                    print(f"{i}.{t}")               
             else:
                   print("NO task added yet.")   
        elif choice =="2": #add task
            new_task = input("Enter a task :").strip()
            task.append(new_task)
            print(f"{new_task} has been added to the list")
        elif choice=="3":  #Remove task
            task_num=int(input("Enter the task you want to remove"))
            if 0< task_num <= len(task):
                removed_task = task.pop(task_num - 1)
                print(f"Task ' {removed_task}' removed.")
            else:
                print("Invalid task number.")
        elif choice=="4": #clear all task
            task.clear()
            print("All tasks cleared ")
        elif choice=="5": #exit
            print("Good bye!")
            break
        else:
            print("invalid option")
to_do_list()