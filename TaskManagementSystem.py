tasks = []

def addTask():
    taskName = input("Enter task name: ")

    try:
        taskPriority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low): "))
        if taskPriority not in [1, 2, 3]:
            raise ValueError("Invalid Priority")
        task = {"taskName" : taskName, "priority" : taskPriority, "completed": False} 
        tasks.append(task)

        print("Task added successfully")
    except ValueError:
        print("Invalid input. Priority must be 1, 2, or 3")

def viewTasks():
    if not tasks:
        print("No tasks to view.\n")
        return
    
    print("Tasks List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not completed"
        priority = ["High", "Medium", "Low"][task["priority"] - 1]
        print(f"{i}. Task: {task['taskName']} | Priority: {priority} | Status: {status}")
    print()

def markTaskCompleted():
    taskToComplete = input("Enter the name of the task to mark as completed: ")

    for task in tasks:
        if task["taskName"].lower() == taskToComplete.lower():
            task["completed"] = True
            print(f"Task '{taskToComplete}' marked as completed.")
            return
        
    print("Task not found")

def main():
    print("Welcome to Task Management System!")

    print("\nWhat would you like to do?")
    
    while True:     
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Exit")
    
        try: 
            choice = int(input("Enter choice: "))

            if choice == 1:
                addTask()
            elif choice == 2:
                viewTasks()
            elif choice == 3:
                markTaskCompleted()
            elif choice == 4:
                print("Thank you for using the Task Management System!")
                break
            else:
                print("Invalid choice, please pick from 1-4")
        except ValueError:
            print("Invalid input. Please try again.\n")

main()