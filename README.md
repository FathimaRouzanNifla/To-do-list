# To-Do List CLI Application

A command-line To-Do list application built with Python, SQLite, and Rich for beautiful terminal output.  
Includes AI-powered task suggestions and supports task creation, completion, deletion, update, and search.

---

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- Update task descriptions
- Search tasks by keyword
- Get AI-generated task suggestions (requires OpenAI API key)
- Persistent storage using SQLite database
- User-friendly CLI interface with Rich library

---

## Requirements

- Python 3.8 or higher
- `rich` library
- Internet connection for AI features
- OpenAI API key for AI suggestions (optional)

---

## Setup & Installation

1. Clone this repository or download the source code.

2. Install required Python packages:

```bash
pip install rich

3. Set your OpenAI API key as an environment variable (to enable AI suggestions):

      On Linux/macOS:
      ```bash
      export OPENAI_API_KEY="your_api_key_here"
      
      On Windows (Command Prompt):

      cmd
      setx OPENAI_API_KEY "your_api_key_here"
      Restart your terminal/command prompt after setting the environment variable.

4. Run the application:
```bash
python main.py


**Usage**
When running the application, you will see a menu:

Add Task

Complete Task

Delete Task

Update Task

Search Tasks

AI Suggestions

Exit

Follow the prompts to manage your tasks.

**Project Structure**
main.py — Entry point, runs the CLI loop asynchronously

cli.py — Handles user input, displays tasks, menus, and interactions

models.py — Defines database models and task management logic with SQLite

ai_helper.py — Communicates with OpenAI API for AI task suggestions

**Notes**
The application currently uses a demo user with user_id = 1 for simplicity.

The SQLite database (todo.db) is created automatically on first run.

AI suggestions require an active OpenAI API key and internet connection.

Make sure to monitor your OpenAI usage and billing if using AI features.

---Let me know if you want me to help create or improve any other part!---



