from sqlalchemy import select, create_engine, select
from sqlalchemy.orm import Session
from create_database import DBMS_NAME, create_db
from Tables import Rentals, Stations
from load_data import df_to_db, load_csv_to_pd_df, read_csv_and_db_name_from_argv, path
import wrm_service as ws

def find_all_rentals_by_return_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rentals).join(Stations, Rentals.return_station_id == Stations.station_id).where(Stations.station_name == station_name)
        rentals = session.execute(statement).all()
        return rentals


def find_all_rentals_by_rental_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rentals).join(Stations, Rentals.rental_station_id == Stations.station_id).where(Stations.station_name == station_name)
        rentals = session.execute(statement).all()
        return rentals

def find_all_stations(engine):
    with Session(engine) as session:
        statement = select(Stations)
        stations = session.execute(statement).all()
        return stations

def find_all_rentals_with_same_rental_and_return(station_name, engine):
    with Session(engine) as session:
        statement = select(Rentals).join(Stations, Rentals.rental_station_id == Stations.station_id).where(Stations.station_name == station_name).filter(Rentals.rental_station_id == Rentals.return_station_id)
        rentals = session.execute(statement).all()
        return rentals

if __name__ == "__main__":
    csv, db = read_csv_and_db_name_from_argv()

    if not path.exists(db + ".db"):
        create_db(db)
        engine = create_engine(f"{DBMS_NAME}:///{db}.db")
        df_to_db(load_csv_to_pd_df(csv), engine)
    else:
        engine = create_engine(f"{DBMS_NAME}:///{db}.db")
    
    # testing
    # find_all_rentals_with_same_rental_and_return("Plac Uniwersytecki (UWr)", engine)
    # find_all_by_rental_station("Plac Uniwersytecki (UWr)", engine)
    # print("-" * 120)
    # find_all_by_return_station("Plac Uniwersytecki (UWr)", engine)
    # find_all_stations(engine)
    # print(ws.calculate_average_ride_time(find_all_by_rental_station("Plac Uniwersytecki (UWr)", engine)))
    # print(ws.calculate_no_of_bikes_on_station(find_all_by_rental_station("Plac Uniwersytecki (UWr)", engine)))
