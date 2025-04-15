from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


DB_PATH = "sqlite:///data.db"

engine = create_engine(DB_PATH, echo=True)
Session = sessionmaker(bind=engine)
