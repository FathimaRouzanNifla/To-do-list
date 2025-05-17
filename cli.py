from rich.console import Console
from rich.table import Table
from models import ToDoManager, Task
import asyncio
from ai_helper import get_task_suggestions  # Your AI helper function

console = Console()

class ToDoCLI:
    def __init__(self):
        self.manager = ToDoManager()
        self.current_user_id = 1  # Demo user ID, replace with real auth later

    def display_tasks(self, tasks: list[Task]):
        """Render tasks in a rich table."""
        table = Table(title="Your Tasks", show_header=True)
        table.add_column("ID", style="cyan")
        table.add_column("Description", style="magenta")
        table.add_column("Status", style="green")

        for task in tasks:
            status = "✓" if task.completed else " "
            table.add_row(str(task.id), task.description, status)
        
        console.print(table)

    async def _get_ai_suggestions(self):
        prompt = console.input("Enter a topic for AI task suggestions: ")
        console.print("Getting AI suggestions...")
        suggestions = await get_task_suggestions(prompt)
        console.print("\nAI Task Suggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            console.print(f"{i}. {suggestion.strip()}")
        console.input("\nPress Enter to return to menu...")

    async def run(self):
        """Main CLI loop."""
        while True:
            tasks = self.manager.get_tasks(user_id=self.current_user_id)
            self.display_tasks(tasks)

            choice = console.input(
                "\n1. Add Task\n"
                "2. Complete Task\n"
                "3. Delete Task\n"
                "4. Update Task Description\n"
                "5. Search Tasks\n"
                "6. AI Suggestions\n"
                "7. Exit\n> "
            )
            
            if choice == "1":
                description = console.input("Task description: ")
                self.manager.add_task(Task(None, description, False, self.current_user_id))
            elif choice == "2":
                try:
                    task_id = int(console.input("Enter task ID to complete: "))
                    if self.manager.complete_task(task_id):
                        console.print("[green]Task marked as completed.[/green]")
                    else:
                        console.print("[red]Task not found.[/red]")
                except ValueError:
                    console.print("[red]Invalid input. Please enter a valid task ID.[/red]")
            elif choice == "3":
                try:
                    task_id = int(console.input("Enter task ID to delete: "))
                    if self.manager.delete_task(task_id):
                        console.print("[green]Task deleted.[/green]")
                    else:
                        console.print("[red]Task not found.[/red]")
                except ValueError:
                    console.print("[red]Invalid input. Please enter a valid task ID.[/red]")
            elif choice == "4":
                try:
                    task_id = int(console.input("Enter task ID to update: "))
                    new_desc = console.input("Enter new task description: ")
                    if self.manager.update_task(task_id, new_desc):
                        console.print("[green]Task updated.[/green]")
                    else:
                        console.print("[red]Task not found or update failed.[/red]")
                except ValueError:
                    console.print("[red]Invalid input. Please enter a valid task ID.[/red]")
            elif choice == "5":
                keyword = console.input("Enter keyword to search tasks: ")
                results = self.manager.search_tasks(self.current_user_id, keyword)
                if results:
                    console.print(f"[blue]Search results for '{keyword}':[/blue]")
                    self.display_tasks(results)
                else:
                    console.print("[yellow]No tasks found matching the keyword.[/yellow]")
                console.input("\nPress Enter to return to menu...")
            elif choice == "6":
                await self._get_ai_suggestions()
            elif choice == "7":
                console.print("Goodbye!")
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
