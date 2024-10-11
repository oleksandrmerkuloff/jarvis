import json
import os
from datetime import datetime

from task import Task


BASE_DIR = os.path.dirname(__file__)


class Jarvis:
    def __init__(self) -> None:
        self.my_tasks = json.load()

    def collect_data():
        title = input("Enter task title: ")
        content = input("Enter task content: ")
        status = input("Enter task status: ")
        theme = input("Enter task theme(optional): ")
        data = {
            'title': title,
            'content': content,
            'status': status,
            'theme': theme,
            'creation_date': datetime.now().strftime('%Y:%m:%d %H:%M'),
            'updated_date': datetime.now().strftime('%Y:%m:%d %H:%M')
        }
        return data

    def create_task(self):
        data = self.collect_data()
        new_task_id = len(self.my_tasks) + 1
        new_task = Task(new_task_id, data)
        self.my_tasks.append(new_task)
        return 'Task was added'

    def update_task(self):
        pass


if __name__ == "__main__":
    new_task = Task("Test1", "Some text", "Dev")
    print(new_task)
    # print(BASE_DIR)
