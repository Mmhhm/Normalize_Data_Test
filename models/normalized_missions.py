from db import db

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)
    target = db.relationship('Target', uselist=False)

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)
    target = db.relationship('Target', uselist=False)

class Coordinate(db.Model):
    __tablename__ = 'coordinates'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 6), nullable=True)
    longitude = db.Column(db.Numeric(10, 6), nullable=True)
    target = db.relationship('Target', uselist=False)

class Target(db.Model):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    coordinate_id = db.Column(db.Integer, db.ForeignKey('coordinates.id'), nullable=False)
    target_type = db.Column(db.String(100), nullable=True)
    industry = db.Column(db.String(100), nullable=True)
    priority = db.Column(db.String(5), nullable=True)
    target = db.relationship('Mission', uselist=False)


class Mission(db.Model):
    __tablename__ = 'missions'
    mission_id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    mission_date = db.Column(db.DATE)
    theater_of_operations = db.Column(db.String(100))
    country = db.Column(db.String(100))
    air_force = db.Column(db.String(100))
    unit_id = db.Column(db.String(100))
    aircraft_series = db.Column(db.String(100))
    callsign = db.Column(db.String(100))
    mission_type = db.Column(db.String(100))
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
    source_id = db.Column(db.String(100))
