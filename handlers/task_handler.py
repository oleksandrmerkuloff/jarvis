from base_handler import BaseHandler
from models.task import Task


class GoalHandler(BaseHandler):
    def __init__(self, db, model=Task):
        super().__init__(db, model)
