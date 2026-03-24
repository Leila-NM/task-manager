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
    descript = input("Enter a task description: ")
    tasks.append({
        "description": descript,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
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
            print(f"{index}. {task}")

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


def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['description']} [{status}]")

    try:
        task_num = int(input("Enter the task number to mark as completed: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
            save_tasks(tasks)
            print("Task status updated.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
