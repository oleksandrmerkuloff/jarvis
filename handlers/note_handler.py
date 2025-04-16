from base_handler import BaseHandler
from models.note import Note


class GoalHandler(BaseHandler):
    def __init__(self, db, model=Note):
        super().__init__(db, model)
