import json
from datetime import datetime


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
    priority = input("Enter priority (High / Medium / Low): ").capitalize()
    due_date = input("Enter task due date (YYYY-MM-DD): ").strip()

    if not descript:
        print("Task description cannot be empty.")
        return

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority.")
        return

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    tasks.append({
        "description": descript,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    })

    save_tasks(tasks)
    print("Task added successfully.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            due = task.get("due_date", "No date")
            priority = task.get("priority", "Low")

            print(
                f"{index}. {task['description']} [{status}] ({priority}) (Due: {due})")


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


def search_tasks(tasks, keyword, completed=None):
    keyword = keyword.lower()

    filtered = filter_tasks(tasks, completed)

    return [
        task for task in filtered
        if keyword in task["description"].lower()
    ]


def search_tasks_ui(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    print("1. Search all tasks")
    print("2. Search Completed tasks")
    print("3. Search Pending tasks")

    choice = input("Choose a filter option: ")

    if choice == "1":
        results = search_tasks(tasks, keyword)

    elif choice == "2":
        results = search_tasks(tasks, keyword, completed=True)

    elif choice == "3":
        results = search_tasks(tasks, keyword, completed=False)

    else:
        print("Invalid choice.")
        return

    display_tasks(results)


def sort_tasks_by_priority(tasks):
    priority_order = {"High": 3, "Medium": 2, "Low": 1}

    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order.get(task.get("priority", "Low"), 1),
        reverse=True
    )

    print("\nTasks sorted by priority:")
    display_tasks(sorted_tasks)


def get_overdue_tasks(tasks):
    today = datetime.today().date()
    result = []

    for task in tasks:
        if "due_date" not in task:
            continue

        due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()

        if not task["completed"] and due_date < today:
            result.append(task)

    return sorted(result, key=lambda t: {"High": 3, "Medium": 2, "Low": 1}.get(t.get("priority", "Low"), 1), reverse=True)


def get_tasks_due_today(tasks):
    today = datetime.today().date()
    result = []

    for task in tasks:
        if "due_date" not in task:
            continue

        due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()

        if not task["completed"] and due_date == today:
            result.append(task)

    return sorted(result, key=lambda t: {"High": 3, "Medium": 2, "Low": 1}.get(t.get("priority", "Low"), 1), reverse=True)


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
        print("7. Search Tasks")
        print("8. Sort Tasks by Priority")
        print("9. View Overdue Tasks")
        print("10. View Tasks Due Today")
        print("11. Exit")

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
            search_tasks_ui(tasks)

        elif choice == "8":
            sort_tasks_by_priority(tasks)

        elif choice == "9":
            overdue = get_overdue_tasks(tasks)
            print("\nOverdue Tasks:")
            display_tasks(overdue)

        elif choice == "10":
            today_tasks = get_tasks_due_today(tasks)
            print("\nTasks Due Today:")
            display_tasks(today_tasks)

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
