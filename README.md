1. **TodoList Class**: 
   - Defines a class `TodoList` to manage tasks.
   - Initializes an empty list to store tasks.

2. **Methods**:
   - `add_task(task)`: Appends a task to the list.
   - `delete_task(index)`: Removes a task at the specified index.
   - `mark_task_completed(index)`: Marks a task at the specified index as completed.
   - `display_tasks()`: Displays all tasks in the list.

3. **Main Functionality**:
   - The `main()` function serves as the entry point.
   - Displays a menu with options for adding, deleting, marking tasks, displaying tasks, and exiting.
   - Depending on the user's choice, it performs the corresponding action using methods of the `TodoList` class.
   - Continues to prompt the user until they choose to exit.

4. **Input Handling**:
   - Validates user inputs to ensure they are within the appropriate range or format.
   - Provides error messages for invalid inputs.

5. **Execution**:
   - The program executes the `main()` function when run.
   - Users interact with the application through the command-line interface, entering numeric choices to perform actions on their to-do list.
