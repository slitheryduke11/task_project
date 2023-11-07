# Create task list
task_list = []


# Add functions for task management
def add_task(task):
    task_list.append(task)


def complete_task():
    task_list.pop()


def show_tasks():
    print("Pending tasks:")
    for i, task in enumerate(task_list):
        print(f"{i + 1}. {task}")


def get_option():
    option = int(input("Enter option: "))
    return option


def print_menu():
    print("Main menu")
    print("1. Add task")
    print("2. Complete task")
    print("3. Show task list")
    print("4. Exit\n")


# Create main function
def main():
    while True:
        print_menu()
        option = get_option()
        if option == 1:
            task = input("Write the new task: ")
            add_task(task)
        elif option == 2:
            complete_task()
        elif option == 3:
            show_tasks()
        elif option == 4:
            break
        else:
            print("Invalid option\n")


# Call main function
if __name__ == "__main__":
    main()
    