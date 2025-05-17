class ToDoManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        self.tasks.append({"id": self.next_id, "task": task, "completed": False})
        self.next_id += 1

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"✅ Task {task_id} marked as completed.")
                return
        print(f"⚠️ Task with ID {task_id} not found.")
