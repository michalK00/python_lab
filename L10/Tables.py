from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

RENTALS_TABLE_NAME = "rentals"
STATIONS_TABLE_NAME = "stations"


# from the CSV it seems like all attributes are required
class Base(DeclarativeBase):
    pass


class Stations(Base):
    __tablename__ = STATIONS_TABLE_NAME
    station_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    station_name: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        return f"station_id: {self.station_id} station_name: {self.station_name}"


class Rentals(Base):
    __tablename__ = RENTALS_TABLE_NAME
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[DateTime] = mapped_column(DateTime)
    end_time: Mapped[DateTime] = mapped_column(DateTime)

    rental_station_id: Mapped[str] = mapped_column(ForeignKey("stations.station_id"))
    return_station_id: Mapped[str] = mapped_column(ForeignKey("stations.station_id"))

    rental_station = relationship("Stations", foreign_keys=[rental_station_id])
    return_station = relationship("Stations", foreign_keys=[return_station_id])

    def __repr__(self) -> str:
        return f"id: {self.id} bike_number: {self.bike_number} rental_station_id: {self.rental_station_id} return_station_id: {self.return_station_id}"