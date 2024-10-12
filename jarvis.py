import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(__file__)


class Jarvis:
    def __init__(self) -> None:
        self.tasks = {}

    def collect_task_data(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        status = input("Enter task status: ")
        theme = input("Enter task theme: ")
        data = {
            'title': title,
            'description': description,
            'status': status,
            'theme': theme,
            'created_date': datetime.now().strftime('%Y:%m:%d %H:%M'),
            'updated_date': datetime.now().strftime('%Y:%m:%d %H:%M')
        }
        return data

    def create_task(self):
        task_data = self.collect_task_data()
        if self.tasks.keys():
            task_id = max(self.tasks) + 1
        else:
            task_id = 1
        self.tasks[task_id] = task_data

    def update_task(self, task_id):
        print('Columns: title, description, status, theme')
        to_update = input('Enter what column whould you like to update: ').lower()

        if to_update not in self.tasks[task_id].keys():
            print("Wrong column, try again")
            return False

        new_data = input('Write new data for this column: ')
        self.tasks[task_id][to_update] = new_data
        return True


if __name__ == "__main__":
    jar = Jarvis()
    jar.create_task()
    print(jar.tasks)
    jar.create_task()
    print(jar.tasks)
    jar.update_task(2)
    print(jar.tasks)
