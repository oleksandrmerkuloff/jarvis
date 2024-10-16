import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(__file__)


class Jarvis:
    START_MESSAGE = """
    Good day sir, my name's Jarvis and I'm your task manager.
    I'm currently in development and you may not have all of my features.
    Here list of command for work with me:
        'help' - show this message again;
        'skip update' - on/off autoupdate file with tasks;
        'show' - show tasks list;
        'create' - load create task algorithm;
        'update' - load update task algorithm;
        'delete' - delete selected task;
        'clear' - for clear your screen;
        'exit' - if you need to go use this command;
    """

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self) -> None:
        self.tasks = self.get_tasks_data()
        self.autoupdate_data_file = False

    def data_file_update(self):
        if self.autoupdate_data_file:
            self.autoupdate_data_file = False
            print('Autoupdate off')
        else:
            self.autoupdate_data_file = True
            print('Autoupdate on')

    def create_data_file(self):
        with open(BASE_DIR + '/tasks.json', 'w') as data_file:
            json.dump({}, data_file)

    def get_tasks_data(self):
        if not os.path.exists(BASE_DIR + '/tasks.json'):
            self.create_data_file()

        with open(BASE_DIR + '/tasks.json', 'r') as data_file:
            return json.load(data_file)

    def save_tasks(self):
        with open(BASE_DIR + '/tasks.json', 'w') as data_file:
            json.dump(self.tasks, data_file)

    def get_current_date(self):
        return datetime.now().strftime('%Y:%m:%d %H:%M')

    def collect_task_data(self):
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        status = input("Enter task status: ").strip()
        theme = input("Enter task theme: ").strip()
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
            task_id = int(list(self.tasks.keys())[-1]) + 1
        else:
            task_id = 1
        self.tasks[str(task_id)] = task_data

        if self.autoupdate_data_file:
            self.save_tasks()
        else:
            update_request = input('Do you want to update data file?(y/n)\n').strip()
            if update_request.lower() == 'y':
                self.save_tasks()

    def update_task(self, task_id):
        if not self.tasks:
            print('I doesn\'t have any task yet!')
            return
        print('Columns: title, description, status, theme')
        to_update = input('Enter what column whould you like to update: ').lower().strip()

        if to_update not in self.tasks[task_id].keys():
            print("Wrong column, try again")
            return False

        new_data = input('Write new data for this column: ').strip()
        self.tasks[task_id][to_update] = new_data
        self.tasks[task_id]['updated_date'] = self.get_current_date()

        if self.autoupdate_data_file:
            self.save_tasks()
        else:
            update_request = input('Do you want to update data file?(y/n)\n')
            if update_request.lower() == 'y':
                self.save_tasks()

    def delete_task(self, task_id):
        task_title = self.tasks[task_id]['title']
        confirm_request = input(f'Are you sure about deleting: {task_title} task? y/n\n').lower().strip()

        if confirm_request == 'y':
            del self.tasks[task_id]

            if self.autoupdate_data_file:
                self.save_tasks()
            else:
                update_request = input('Do you want to update data file?(y/n)\n')
                if update_request.lower() == 'y':
                    self.save_tasks()
        else:
            print('Confirmation error, operation cancelled....')

    def show_tasks(self, task_optional):
        if not self.tasks:
            print('I doesn\'t have any task yet!')
            return
        for task_id, task in self.tasks.items():
            if task_optional != 'all':
                if (task['status'].lower() != task_optional.lower() and
                   task['theme'].lower() != task_optional.lower()):
                    continue
                if task['theme'].lower() == task_optional.lower():
                    if task['status'].lower() == 'done':
                        continue
            print()
            print(f'Task id: {task_id}')
            for key, info in task.items():
                print(f'{key.title()}: {info}')
        print()

    def run(self):
        print(self.START_MESSAGE)
        while True:
            user_request = input('Wait for your commands here: ').lower().strip()
            if user_request == 'help':
                print(self.START_MESSAGE)
            elif user_request == 'skip update':
                self.data_file_update()
            elif user_request == 'show':
                print('Do you want to see full list of tasks or with special status: ')
                task_status = input('Type "all" or special status/theme here: ')
                self.show_tasks(task_status)
            elif user_request == 'create':
                self.create_task()
            elif user_request == 'update':
                task_id = input('Enter task id: ').strip()
                self.update_task(task_id)
            elif user_request == 'delete':
                task_id = input('Enter task id: ').strip()
                self.delete_task(task_id)
            elif user_request == 'clear':
                Jarvis.clear()
            elif user_request == 'exit':
                if self.tasks != self.get_tasks_data() and self.autoupdate_data_file:
                    self.save_tasks()
                elif self.tasks != self.get_tasks_data():
                    save_request = input('Do you want to update data file?(y/n)\n')
                    if save_request.lower() == 'y':
                        self.save_tasks()
                print("If I will be need for you, just call me...")
                return


if __name__ == "__main__":
    jar = Jarvis()
    jar.run()
