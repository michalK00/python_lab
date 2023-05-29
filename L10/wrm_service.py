import datetime
import wrm_repository as repo


def calculate_average_ride_time_rental_station(station_name, engine):
    rentals = repo.find_all_rentals_by_rental_station(station_name, engine)
    return _calculate_average_ride_time(rentals)

def calculate_average_ride_time_return_station(station_name, engine):
    rentals = repo.find_all_rentals_by_return_station(station_name, engine)
    return _calculate_average_ride_time(rentals)

def calculate_average_ride_time_same_stations(station_name, engine):
    rentals = repo.find_all_rentals_with_same_rental_and_return(station_name, engine)
    return _calculate_average_ride_time(rentals)

def calculate_no_of_bikes_on_station(station_name, engine):
    rentals = repo.find_all_rentals_by_return_station(station_name, engine)
    unique_bikes_set = set([rental[0].bike_number for rental in rentals])
    return len(unique_bikes_set)

def calculate_no_bikes_with_same_stations(station_name, engine):
    rentals = repo.find_all_rentals_with_same_rental_and_return(station_name, engine)
    return len(rentals)

def find_get_all_stations(engine):
    return repo.find_all_stations(engine)

def _calculate_average_ride_time(rentals):
    ride_times = [rental[0].end_time - rental[0].start_time for rental in rentals]
    if len(ride_times) != 0:
        return sum(ride_times, datetime.timedelta(0)) / len(ride_times)
    else:
        return 0