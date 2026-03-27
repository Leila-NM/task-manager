import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    descript = input("Enter a task description: ").strip()

    if not descript:
        print("Task description cannot be empty.")
        return

    tasks.append({
        "description": descript,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. {task['description']} [{status}]")


def delete_task(tasks):
    if not tasks:
        print("There are no tasks to delete")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']}")

        try:
            task_num = int(input("Enter the task number to delete: "))

            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def toggle_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['description']} [{status}]")

    try:
        task_num = int(
            input("Enter the task number to mark as Complete/Incomplete: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]

            task = tasks[task_num - 1]
            status = "completed ✓" if task["completed"] else "marked as pending ✗"

            save_tasks(tasks)
            print(f"Task {status}.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def filter_tasks(tasks, completed=None):
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]


def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View pending Tasks")
        print("5. Toggle Task Completion")
        print("6. Delete task")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(filter_tasks(tasks))

        elif choice == "3":
            display_tasks(filter_tasks(tasks, completed=True))

        elif choice == "4":
            display_tasks(filter_tasks(tasks, completed=False))

        elif choice == "5":
            toggle_task(tasks)

        elif choice == "6":
            delete_task(tasks)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
