from task_manager.task_utils import tasks, add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            view_pending_tasks(tasks)
            if any(not t["completed"] for t in tasks):
                try:
                    index = int(input("Enter task number to mark as complete: "))
                    mark_task_as_complete(index, tasks)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            total = len(tasks)
            completed = sum(1 for t in tasks if t["completed"])
            progress = calculate_progress(tasks)
            print(f"\nProgress: {completed}/{total} tasks completed ({progress:.1f}%)")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
