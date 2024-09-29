from enum import unique

from db import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), unique=True, nullable=True)




class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), unique=True, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)




class Coordinate(db.Model):
    __tablename__ = 'coordinates'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Numeric(10, 6), nullable=True)
    longitude = db.Column(db.Numeric(10, 6), nullable=True)




class Target(db.Model):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    coordinate_id = db.Column(db.Integer, db.ForeignKey('coordinates.id'), nullable=True)
    target_type = db.Column(db.String(300), nullable=True)
    industry = db.Column(db.String(300), nullable=True)
    priority = db.Column(db.String(300), nullable=True)




class Mission(db.Model):
    __tablename__ = 'missions'
    mission_id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    mission_date = db.Column(db.DATE)
    theater_of_operations = db.Column(db.String(300))
    country = db.Column(db.String(300))
    air_force = db.Column(db.String(300))
    unit_id = db.Column(db.String(300))
    aircraft_series = db.Column(db.String(300))
    callsign = db.Column(db.String(300))
    mission_type = db.Column(db.String(300))
    takeoff_base = db.Column(db.String(255))
    takeoff_location = db.Column(db.String(255))
    takeoff_latitude = db.Column(db.String(15))
    takeoff_longitude = db.Column(db.Numeric(10, 6))
    target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    altitude_hundreds_of_feet = db.Column(db.Numeric(7, 2))
    airborne_aircraft = db.Column(db.Numeric(4, 1))
    attacking_aircraft = db.Column(db.Integer)
    bombing_aircraft = db.Column(db.Integer)
    aircraft_returned = db.Column(db.Integer)
    aircraft_failed = db.Column(db.Integer)
    aircraft_damaged = db.Column(db.Integer)
    aircraft_lost = db.Column(db.Integer)
    high_explosives = db.Column(db.String(255))
    high_explosives_type = db.Column(db.String(255))
    high_explosives_weight_pounds = db.Column(db.String(25))
    high_explosives_weight_tons = db.Column(db.Numeric(10, 2))
    incendiary_devices = db.Column(db.String(255))
    incendiary_devices_type = db.Column(db.String(255))
    incendiary_devices_weight_pounds = db.Column(db.Numeric(10, 2))
    incendiary_devices_weight_tons = db.Column(db.Numeric(10, 2))
    fragmentation_devices = db.Column(db.String(255))
    fragmentation_devices_type = db.Column(db.String(255))
    fragmentation_devices_weight_pounds = db.Column(db.Numeric(10, 2))
    fragmentation_devices_weight_tons = db.Column(db.Numeric(10, 2))
    total_weight_pounds = db.Column(db.Numeric(10, 2))
    total_weight_tons = db.Column(db.Numeric(10, 2))
    time_over_target = db.Column(db.String(8))
    bomb_damage_assessment = db.Column(db.String(255))
    source_id = db.Column(db.String(300))


    def to_dict(self):
        return {
            "date": self.mission_date,
            "theater_of_operations": self.theater_of_operations,
            "country": self.country,
            "air_force": self.air_force,
            "unit_id": self.unit_id,
            "aircraft_series": self.aircraft_series,
            "callsign": self.callsign,
            "mission_type": self.mission_type,
            "takeoff_base": self.takeoff_base,
            "takeoff_location": self.takeoff_location,
            "takeoff_latitude": self.takeoff_latitude,
            "takeoff_longitude": self.takeoff_longitude,
            "target_id": self.target_id,
            "altitude_hundreds_of_feet": self.altitude_hundreds_of_feet,
            "airborne_aircraft": self.airborne_aircraft,
            "attacking_aircraft": self.attacking_aircraft,
            "bombing_aircraft": self.bombing_aircraft,
            "aircraft_returned": self.aircraft_returned,
            "aircraft_failed": self.aircraft_failed,
            "aircraft_damaged": self.aircraft_damaged,
            "aircraft_lost": self.aircraft_lost,
            "high_explosives": self.high_explosives,
            "high_explosives_type": self.high_explosives_type,
            "high_explosives_weight_pounds": self.high_explosives_weight_pounds,
            "high_explosives_weight_tons": self.high_explosives_weight_tons,
            "incendiary_devices": self.incendiary_devices,
            "incendiary_devices_type": self.incendiary_devices_type,
            "incendiary_devices_weight_pounds": self.incendiary_devices_weight_pounds,
            "incendiary_devices_weight_tons": self.incendiary_devices_weight_tons,
            "fragmentation_devices": self.fragmentation_devices,
            "fragmentation_devices_type": self.fragmentation_devices_type,
            "fragmentation_devices_weight_pounds": self.fragmentation_devices_weight_pounds,
            "fragmentation_devices_weight_tons": self.fragmentation_devices_weight_tons,
            "total_weight_pounds": self.total_weight_pounds,
            "total_weight_tons": self.total_weight_tons,
            "time_over_target": self.time_over_target,
            "bomb_damage_assessment": self.bomb_damage_assessment,
            "source_id": self.source_id,
        }
