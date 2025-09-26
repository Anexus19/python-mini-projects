tasks = []

while True:
    # title + options
    print("\nPython Task Manager") 
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")

    # ask every time
    chosen_answer = input("Choose: ")

    if chosen_answer == "1":
        task = input("Type the task needed: ")
        tasks.append(task)
        print("Task added!")

    elif chosen_answer == "2":
        if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

    elif chosen_answer == "3":
        task_to_remove = input("Which task to remove? ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print("Task removed!")
        else:
            print("Task not found.")

    elif chosen_answer == "4":
        print("Exiting Task Manager")
        break   # ← stops the loop

    else:
        print("Invalid choice.")
