import wrm_service as srv


def get_all_stations(engine):
    return srv.find_get_all_stations(engine)

def get_average_ride_time_on_return_station(station_name, engine):
    return srv.calculate_average_ride_time_return_station(station_name, engine)

def get_average_ride_time_on_rental_station(station_name, engine):
    return srv.calculate_average_ride_time_rental_station(station_name, engine)

def get_bike_no_on_return_station(station_name, engine):
    return srv.calculate_no_of_bikes_on_station(station_name, engine)

def get_average_ride_time_for_bikes_with_same_stations(station_name, engine):
    return srv.calculate_average_ride_time_same_stations(station_name, engine)

def get_no_bikes_with_same_stations(station_name, engine):
    return srv.calculate_no_bikes_with_same_stations(station_name, engine)