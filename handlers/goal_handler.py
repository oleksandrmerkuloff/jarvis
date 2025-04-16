from base_handler import BaseHandler
from models.goal import Goal


class GoalHandler(BaseHandler):
    def __init__(self, db, model=Goal):
        super().__init__(db, model)
