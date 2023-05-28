from Tables import Base
from sqlalchemy import create_engine
from sys import argv
from os import path

DBMS_NAME = "sqlite"
 


def read_db_name_from_argv() -> str:
    if len(argv) != 2:
        raise IndexError(
            "You have input incorrect amount of arguments! "
            "Please give 1 argument, that will be the name of the database."
        )

    if path.exists(f"{argv[1]}.db"):
        raise Warning("Database with given name already exists! Be cautious next time.")

    return argv[1]


def create_db(db_name: str) -> None:
    engine = create_engine(f"{DBMS_NAME}:///{db_name}.db")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db(read_db_name_from_argv())
