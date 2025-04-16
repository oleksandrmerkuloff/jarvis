from typing import Optional, Any

from sqlalchemy import select
from sqlalchemy.orm import Session, DeclarativeMeta
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm.exc import ObjectDeletedError


class BaseHandler:
    def __init__(self, db: Session, model: DeclarativeMeta = None) -> None:
        self.db = db
        self.model = model

    def get_record_by_id(self, id: int) -> Optional[DeclarativeMeta]:
        record = self.db.get(self.model, id)
        if not record:
            raise NoResultFound('Record doesn\'t exist.')
        return record

    def get_record_by_attr(
            self,
            key: str,
            value: Any
            ) -> Optional[DeclarativeMeta]:

        if not hasattr(self.model, key):
            raise AttributeError('Model doesn\'t have this attr!')

        stmt = select(self.model).where(getattr(self.model, key) == value)
        record = self.db.execute(stmt).scalar_one_or_none()

        if not record:
            raise NoResultFound(f"No record found for {key} = {value}")
        return record

    def add_record(self, data: dict) -> bool:
        try:
            record = self.model(**data)
            self.db.add(record)
        except Exception:
            self.db.rollback()
            return False
        else:
            self.db.commit()
        return True

    def update_record(self, id: int, data: dict) -> bool:
        record = self.get_record_by_id(id)
        try:
            for key, value in data.items():
                setattr(record, key, value)
        except SQLAlchemyError:
            return False
        else:
            self.db.commit()
        return True

    def delete_record(self, id: int) -> bool:
        record = self.get_record_by_id(id)
        try:
            self.db.delete(record)
        except ObjectDeletedError:
            self.db.rollback()
            return False
        else:
            self.db.commit()
        return True
