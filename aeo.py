class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def mark_task_completed(self, index):
        self.tasks[index] += " (Completed)"

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == "2":
            if not todo_list.tasks:
                print("No tasks to delete.")
            else:
                index = int(input("Enter the index of the task to delete: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    todo_list.delete_task(index)
                    print("Task deleted successfully!")
                else:
                    print("Invalid index.")
        elif choice == "3":
            if not todo_list.tasks:
                print("No tasks to mark as completed.")
            else:
                index = int(input("Enter the index of the task to mark as completed: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    todo_list.mark_task_completed(index)
                    print("Task marked as completed successfully!")
                else:
                    print("Invalid index.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
