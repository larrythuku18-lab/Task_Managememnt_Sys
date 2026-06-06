from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []


def create_task(title, description, due_date):
    return {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }


def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)
    task = create_task(title, description, due_date)
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    if tasks[index - 1]["completed"]:
        print("Task is already marked as complete.")
        return
    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    print("\nPending Tasks:")
    for t in pending:
        print(f"  [{t['id']}] {t['title']} (Due: {t['due_date']})")
        if t["description"]:
            print(f"       {t['description']}")


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100
