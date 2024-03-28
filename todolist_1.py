class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")

    def add_task(self, task_name):
        task = {"task": task_name, "completed": False}
        self.tasks.append(task)
        print(f"Task '{task_name}' added to your to-do list.")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a valid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            print("Invalid task number. Please enter a valid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                todo_list.mark_completed(task_number)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '4':
            todo_list.display_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
