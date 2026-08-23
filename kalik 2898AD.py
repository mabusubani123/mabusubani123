from collections import deque

tasks = deque()


def add_taks():
    task = input("Enter task:")
    task.append(task)
    print("Task added.")
    
    
def execute_task():
    
    if not tasks:
        print("No tasks avilable.")
    else:
        task = tasks. popleft()
        print("Exeuting:", task)
        
        
def view_tasks():
    
    if not tasks:
        print("No tasks.")
        
    else:
        print("pending Tasks:")
        
        for task in tasks:
            print("_", tasks)
            
            
while True:
    
    print("/n---TASK SCHEDULER---")
    print("1. Add Task")
    print("2. Exeute Task")
    print("3. view Tasks")
    print("4.Exit")
    
    choice = input("Enter choice:")
    
    if choice == "1":
        add_taks()
        
    elif choice == "2":
        execute_task()
        
    elif choice == "3":
        view_tasks()
        
    elif choice =="4":
        break    