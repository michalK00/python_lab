from Tables import Rentals, Stations
from create_database import DBMS_NAME, create_db

from sys import argv
from pandas import read_csv, DataFrame
from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session
from typing import Tuple, List, Dict
from datetime import datetime
from os import path


def read_csv_and_db_name_from_argv() -> Tuple[str, str]:
    if len(argv) != 3:
        raise IndexError(
            "You have input incorrect amount of arguments! "
            "Please give 2 argument, that will be the name CSV and the database."
        )

    csv_name = argv[1]
    db_name = argv[2]

    return csv_name, db_name


def load_csv_to_pd_df(csv_name: str) -> DataFrame:
    if not path.exists(csv_name):
        raise ValueError("Incorrect CSV filename")

    # only 09 had some duplicates (exactly 30), so it is probably just a mistake on their part
    df = read_csv(csv_name)
    df = df.drop_duplicates(subset="UID wynajmu")
    return df


def get_and_add_to_dict_if_new(
        station_name: str, stations_dict: Dict[str, Stations], session: Session
) -> Stations:
    if station_name in stations_dict.keys():
        return stations_dict[station_name]

    statement = select(Stations).where(Stations.station_name == station_name)
    station = session.scalar(statement)

    if station is not None:
        return station

    station = Stations(station_name=station_name)
    # dicts are passed by reference, so this will work fine
    stations_dict[station_name] = station

    return station


def df_to_db(df: DataFrame, db_engine: Engine) -> None:
    # dict works like an accumulator for new stations, so there aren't as many accesses to the database needed
    stations: Dict[str, Stations] = {}
    # not necessary for rentals, as they aren't repeated
    rentals: List[Rentals] = []

    date_format = "%Y-%m-%d %H:%M:%S"

    with Session(db_engine) as session:
        for i, row in df.iterrows():
            rental_id = int(row["UID wynajmu"])
            bike_number = int(row["Numer roweru"])
            start_time = datetime.strptime(row["Data wynajmu"], date_format)
            end_time = datetime.strptime(row["Data zwrotu"], date_format)

            rental_station = get_and_add_to_dict_if_new(
                row["Stacja wynajmu"], stations, session
            )
            return_station = get_and_add_to_dict_if_new(
                row["Stacja zwrotu"], stations, session
            )

            rentals.append(
                Rentals(
                    id=rental_id,
                    bike_number=bike_number,
                    start_time=start_time,
                    end_time=end_time,
                    rental_station=rental_station,
                    return_station=return_station,
                )
            )

        session.add_all(stations.values())
        session.add_all(rentals)
        session.commit()


if __name__ == "__main__":
    csv, db = read_csv_and_db_name_from_argv()

    if not path.exists(db + ".db"):
        create_db(db)

    engine = create_engine(f"{DBMS_NAME}:///{db}.db")

    df_to_db(load_csv_to_pd_df(csv), engine)
