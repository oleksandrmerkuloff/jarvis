from task import Task


class SubTask:
    def __init__(self) -> None:
        self.task_data = Task()
        self.next = None


class Goal:
    def __init__(self) -> None:
        self.head_task = None

    def add_task(self, task: SubTask) -> None:
        if self.head_task is None:
            self.head_task = task
        else:
            current_task = self.head_task
            while current_task.next:
                current_task = current_task.next
            current_task.next = task
