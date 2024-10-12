import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(__file__)


class Jarvis:
    def __init__(self) -> None:
        self.tasks = self.get_tasks_data()

    def create_data_file(self):
        with open(BASE_DIR + '/task.json', 'w') as data_file:
            json.dump({}, data_file)

    def get_tasks_data(self):
        if not os.path.exists(BASE_DIR + '/task.json'):
            self.create_data_file()

        with open(BASE_DIR + '/task.json', 'r') as data_file:
            return json.load(data_file)

    def save_tasks(self):
        with open(BASE_DIR + '/task.json', 'w') as data_file:
            json.dump(self.tasks, data_file)

    def get_current_date(self):
        return datetime.now().strftime('%Y:%m:%d %H:%M')

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
            'created_date': self.get_current_date(),
            'updated_date': self.get_current_date()
        }
        return data

    def create_task(self):
        task_data = self.collect_task_data()
        if self.tasks.keys():
            task_id = max(self.tasks) + 1
        else:
            task_id = 1
        self.tasks[task_id] = task_data

        self.save_tasks()

    def update_task(self, task_id):
        print('Columns: title, description, status, theme')
        to_update = input('Enter what column whould you like to update: ').lower()

        if to_update not in self.tasks[task_id].keys():
            print("Wrong column, try again")
            return False

        new_data = input('Write new data for this column: ')
        self.tasks[task_id][to_update] = new_data
        self.tasks[task_id]['updated_date'] = self.get_current_date()

        self.save_tasks()

    def run(self):
        print('Greetings, sir. My name is Jarvis.')
        print('Type commands for work: <commands list>')
        while True:
            user_request = input('print here: ')
            if user_request == 'create':
                self.create_task()


if __name__ == "__main__":
    jar = Jarvis()
    jar.run()
