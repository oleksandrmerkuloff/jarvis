import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE_DIR = os.getcwd()
ENGINE = create_engine('sqlite://', echo=True)
SESSION = sessionmaker(ENGINE)


def create_db():
    return 'create database in the destination folder'


def check_db():
    return 'If database already exsists'


if __name__ == '__main__':
    print(BASE_DIR)
