from typing import Optional, Union, Type

from sqlalchemy import select
from sqlalchemy.orm import Session, DeclarativeMeta
from sqlalchemy.exc import NoResultFound, SQLAlchemyError


class BaseHandler:
    def __init__(self):
        pass

    def get_record(self):
        pass

    def add_record(self):
        pass

    def edit_record(self):
        pass

    def delete_record(self):
        pass
