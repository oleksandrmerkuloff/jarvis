import sqlite3


class DBHandler:
    def __init__(self) -> None:
        self.con = sqlite3.connect('jarvis.db')
        self.cur = self.con.cursor()

        self.cur.execute('PRAGMA foreign_keys = ON;')

    def get_all_tasks(self):
        pass

    def get_tasks_by_theme(self):
        pass

    def get_tasks_by_state(self):
        pass

    def get_tasks_by_id(self):
        pass

    def get_tasks_by_goal(self):
        pass
