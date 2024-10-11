import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(__file__)


class Jarvis:
    def __init__(self) -> None:
        self.my_tasks = self.read_tasks()

    def read_tasks(self):
        with open(BASE_DIR + '/tasks.json', 'r') as data_file:
            return json.load(data_file)

    def get_current_date(self):
        return datetime.now().strftime('%Y:%m:%d %H:%M')

    def collect_data(self):
        title = input("Enter task title: ")
        content = input("Enter task content: ")
        status = input("Enter task status: ")
        theme = input("Enter task theme(optional): ")
        data = {
            'title': title,
            'content': content,
            'status': status,
            'theme': theme,
            'creation_date': self.get_current_date(),
            'updated_date': self.get_current_date()
        }
        return data

    def create_task(self):
        task_data = self.collect_data()
        if self.my_tasks.keys():
            new_task_id = int(list(self.my_tasks.keys())[-1]) + 1
        else:
            new_task_id = 1
        self.my_tasks[new_task_id] = task_data
        return 'Task was added'

    def update_task(self, id, column, new_data):
        self.my_tasks[id][column] = new_data
        self.my_tasks[id]['updated_date'] = self.get_current_date()

    def write_to_json(self, data):
        with open(BASE_DIR + '/tasks.json', 'w') as data_file:
            json.dump(data, data_file)


if __name__ == "__main__":
    jar = Jarvis()
    jar.create_task()
    jar.write_to_json(jar.my_tasks)
    print(jar.my_tasks)
    # print(BASE_DIR)
