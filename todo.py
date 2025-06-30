tasks = []

def show_menu():
    print("\n1) Add Task\n2) View Tasks\n3) Quit")

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
