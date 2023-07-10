The core classes, functions, and methods that will be necessary for the API are as follows:

1. Task: Represents a single task in the to-do list. It has properties such as name, description, due date, and status.

2. TaskManager: Manages the tasks in the to-do list. It provides methods for adding, editing, marking as complete, and deleting tasks. It also supports filtering and sorting tasks.

3. API: Handles the HTTP requests and routes them to the appropriate methods in the TaskManager. It provides endpoints for adding, editing, marking as complete, deleting, and retrieving tasks.

4. Pagination: Manages the pagination of the task list in the API. It calculates the offset and limit for retrieving a subset of tasks.

5. Sorting: Handles the sorting of tasks based on different criteria such as ID, name, and due date.

Now, let's proceed with creating the necessary files and their contents.

1. `task.py`

