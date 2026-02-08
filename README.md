# Python Console TODO Application

## Project Overview
This is a simple command-line todo application built with Python that allows users to manage tasks via the terminal. The CLI-based approach was chosen to provide a lightweight, fast, and efficient task management solution without the overhead of a graphical interface. This approach is ideal for developers and power users who prefer keyboard-driven workflows.

## Technology Stack
- **Python Version**: 3.12+
- **Standard Library Only**: No external dependencies required
- **JSON Storage**: Built-in `json` module for data persistence
- **File I/O**: Built-in `os` module for file operations

## Project Structure
```
├── main.py                 # Entry point of the application
├── tasks.json             # JSON file storing todo items persistently
├── src/
│   ├── cli/
│   │   └── todo_cli.py   # Command-line interface layer
│   ├── models/
│   │   └── todo_item.py  # Todo item data model
│   ├── services/
│   │   └── todo_service.py # Business logic layer
│   └── utils/
│       └── data_manager.py # JSON persistence layer
└── README.md
```

### main.py
The main entry point of the application that handles command-line arguments and initializes the CLI interface.

### tasks.json
The JSON file where all todo items are persistently stored between application runs. Contains:
- `todos`: Object containing all todo items keyed by ID
- `next_id`: Counter for generating unique IDs

## Step-by-Step Workflow

### Step 1: Running the App
```bash
python main.py [command] [arguments]
```
The application reads from `tasks.json` on startup and writes to it on data changes.

### Step 2: Adding Tasks
```bash
python main.py add "Buy groceries"
```
**Internal Process**:
- The CLI receives the "add" command with description
- Service generates a new unique ID using the data manager
- Creates a new TodoItem with ID, description, priority (default: medium), and due date (optional)
- Saves the new item to `tasks.json` using the DataManager
- Returns confirmation message with the assigned ID

### Step 3: Listing Tasks
```bash
python main.py list
```
**Internal Process**:
- The CLI receives the "list" command
- Service loads all todos from `tasks.json` via DataManager
- Converts stored data to TodoItem objects
- Formats and displays all tasks with their completion status, priority, and due date

### Step 4: Completing Tasks
```bash
python main.py complete 1
```
**Internal Process**:
- The CLI receives the "complete" command with task ID
- Service retrieves the specific task from DataManager
- Updates the task's completion status
- Saves the updated task back to `tasks.json`

### Step 5: Updating Tasks
```bash
python main.py update 1 "Buy groceries and cook dinner"
```
**Internal Process**:
- The CLI receives the "update" command with ID and new description
- Service retrieves the task from DataManager
- Validates the new description
- Updates the task's description
- Saves the changes back to `tasks.json`

### Step 6: Deleting Tasks
```bash
python main.py delete 1
```
**Internal Process**:
- The CLI receives the "delete" command with task ID
- Service removes the task from DataManager
- Updates `tasks.json` to reflect the deletion

## Commands Reference

### Add
Add a new task to your todo list with optional priority and due date
```bash
python main.py add "Task description here" [priority] [due_date]
```
- Priority options: `low`, `medium` (default), `high`
- Due date format: `YYYY-MM-DD` (optional)

### List
Display all tasks with their completion status, priority, and due date
```bash
python main.py list
```

### Complete
Mark a task as completed
```bash
python main.py complete [task_id]
```

### Update
Modify the description of an existing task
```bash
python main.py update [task_id] "New description"
```

### Delete
Remove a task from your list
```bash
python main.py delete [task_id]
```

### Search
Find tasks by keyword in the description
```bash
python main.py search "keyword"
```

### Filter
Show tasks by priority level
```bash
python main.py filter [priority]
```
- Priority options: `low`, `medium`, `high`

### Stats
Display statistics about your tasks
```bash
python main.py stats
```

### Help
Display available commands and usage
```bash
python main.py help
```

## Data Persistence Explanation

The application uses JSON file persistence to maintain task data between application runs. This approach was chosen for its simplicity, readability, and compatibility with the Python standard library.

### How Tasks Are Saved and Loaded
- On application startup, the DataManager loads `tasks.json` if it exists
- When a task is added, updated, or deleted, changes are immediately written to the file
- The JSON structure maintains all task properties: ID, description, completion status, priority, due date, and creation date
- A `next_id` counter ensures unique IDs across application restarts

### Why Persistence Is Important
- **Data Retention**: Tasks remain available after closing and reopening the application
- **User Convenience**: No risk of losing important tasks due to application crashes
- **Cross-Session Continuity**: Users can manage tasks over multiple sessions

## Error Handling

### Invalid Commands
If an unrecognized command is entered, the application displays an error message and suggests valid commands.

### Invalid Task IDs
When attempting to operate on a non-existent task ID, the application shows a clear error message: "Error: Task with ID [id] not found".

### Empty Task List
When the list command is used with no tasks, the application displays "No tasks in your todo list."

## Limitations (Phase 1)

### No GUI
- Pure command-line interface
- No visual interface elements
- Terminal-based interaction only

### No Web Deployment
- Local execution only
- No web interface or server
- No remote access capabilities

### Local Execution Only
- Data stored locally in JSON file
- No cloud synchronization
- No multi-device support

## Future Improvements (Phase 2 Ideas)

### Web Interface
- Flask or Django web application
- Responsive design for multiple devices
- Real-time updates with WebSockets

### Authentication
- User registration and login system
- Personalized todo lists per user
- Secure session management

### Database Storage
- SQLite, PostgreSQL, or MongoDB integration
- More robust data querying capabilities
- Better performance for large datasets

## How to Run (Quick Start)

### Clone Repository
```bash
git clone [repository-url]
cd [repository-name]
```

### Run Commands
```bash
# Add a new task
python main.py add "Learn Python CLI development"

# Add a task with priority and due date
python main.py add "Complete project proposal" high 2026-02-15

# List all tasks
python main.py list

# Complete a task (assuming it has ID 1)
python main.py complete 1

# Update a task (assuming it has ID 1)
python main.py update 1 "Master Python CLI development"

# Delete a task (assuming it has ID 1)
python main.py delete 1

# Search for tasks containing a keyword
python main.py search "project"

# Filter tasks by priority
python main.py filter high

# Show statistics about tasks
python main.py stats

# Get help
python main.py help
```

The application is ready to use immediately after cloning with no additional setup required!