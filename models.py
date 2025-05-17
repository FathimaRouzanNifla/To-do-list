import sqlite3
from dataclasses import dataclass
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Task:
    id: Optional[int]
    description: str
    completed: bool
    user_id: int

class ToDoManager:
    def __init__(self, db_path: str = "todo.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize database with tables."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed BOOLEAN DEFAULT FALSE,
                    user_id INTEGER REFERENCES users(id)
                )
            """)

    def add_task(self, task: Task) -> int:
        """Add a task to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (description, completed, user_id) VALUES (?, ?, ?)",
                (task.description, task.completed, task.user_id)
            )
            conn.commit()
            return cursor.lastrowid

    def get_tasks(self, user_id: int) -> List[Task]:
        """Fetch all tasks for a user."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
            return [Task(**row) for row in cursor.fetchall()]

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tasks SET completed = TRUE WHERE id = ?", (task_id,)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            return cursor.rowcount > 0

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update the description of a task."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def search_tasks(self, user_id: int, keyword: str) -> List[Task]:
        """Search tasks containing keyword in description."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            search_pattern = f"%{keyword}%"
            cursor.execute(
                "SELECT * FROM tasks WHERE user_id = ? AND description LIKE ?", (user_id, search_pattern)
            )
            return [Task(**row) for row in cursor.fetchall()]
