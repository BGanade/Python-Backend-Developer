""" Ana needs a simple program to manage her daily tasks. She wants to be able to add, 
view, and remove tasks from a list.

Create a program with an interactive menu that allows the user to add, view, and remove 
tasks. Use a list to store the tasks.

Example input:
1. Add task
2. View tasks
3. Remove task
4. Exit

Choose an option: 1

Expected output:
Enter the task: Study Python
Task added!

If the user selects option 2 after adding a task:
Tasks:
1. Study Python

If the user selects option 3 with a task already added:
Enter the task number to remove: 1
Task 'Study Python' removed!

If the user selects option 3 without any tasks added:
Enter the task number to remove: Study Python
Error: No tasks to remove.

If the user selects option 3 and enters an invalid value:
Choose an option: 3
Enter the task number to remove: ABC
Error: Invalid input! Please enter a number.

If the user selects an option that is not listed:
Choose an option: 5
Error: Invalid option! Please choose an option between 1 and 4.

If the user selects option 4:
Choose an option: 4
Exiting the task manager. Goodbye! """

def program():
    tasks = []

    while True:
        show_menu()
        option = get_option()
        running = run_option(option, tasks)

        if not running:
            break


def show_menu():
    print(
        "\nOptions:"
        "\n1 - Add Task"
        "\n2 - View Tasks"
        "\n3 - Remove Task"
        "\n4 - Exit Program\n"
    )


def get_option():
    while True:
        try:
            user_option = int(input("Choose an option: "))

            if not 1 <= user_option <= 4:
                print("Error: Invalid option! Please choose an option between 1 and 4.")
            else:
                return user_option

        except ValueError:
            print("Error: Please enter a number.")


def add_task(tasks):
    task = input("Enter the task: ")

    tasks.append(task)

    print(f"Task '{task}' added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task(tasks):
    if not tasks:
        print("Error: No tasks to remove.")
        return

    view_tasks(tasks)

    while True:
        try:
            task_number = int(input("Enter the task number to remove: "))

            if not 1 <= task_number <= len(tasks):
                print("Error: Invalid task number.")
                continue

            removed_task = tasks.pop(task_number - 1)

            print(f"Task '{removed_task}' removed!")
            break

        except ValueError:
            print("Error: Invalid input! Please enter a number.")


def exit_program():
    print("Exiting the task manager. Goodbye!")


def run_option(option, tasks):
    match option:
        case 1:
            add_task(tasks)
            return True

        case 2:
            view_tasks(tasks)
            return True

        case 3:
            remove_task(tasks)
            return True

        case 4:
            exit_program()
            return False


program()