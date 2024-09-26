from itertools import count
from operator import index

from models.normalized_missions import *

def normalize_db(old_missions):
    for mission in old_missions:
        counter = 1
        new_mission = Mission(
            mission_date=mission.mission_date,
            theater_of_operations=mission.theater_of_operations,
            country=mission.country,
            air_force=mission.air_force,
            units_id=mission.units_id,
            aircraft_series=mission.aircraft_series,
            callsign=mission.callsign,
            mission_type=mission.mission_type,
            takeoff_base=mission.takeoff_base,
            takeoff_location=mission.takeoff_location,
            takeoff_latitude=mission.takeoff_latitude,
            takeoff_longitude=mission.takeoff_longitude,
            target_id=counter,
            altitude_hundreds_of_feet=mission.altitude_hundreds_of_feet,
            airborne_aircraft=mission.airborne_aircraft,
            attacking_aircraft=mission.attacking_aircraft,
            bombing_aircraft=mission.bombing_aircraft,
            aircraft_returned=mission.aircraft_returned,
            aircraft_failed=mission.aircraft_failed,
            aircraft_damaged=mission.aircraft_damaged,
            aircraft_lost=mission.aircraft_lost,
            high_explosives=mission.high_explosives,
            high_explosives_type=mission.high_explosives_type,
            high_explosives_weight_pounds=mission.high_explosives_weight_pounds,
            high_explosives_weight_tons=mission.high_explosives_weight_tons,
            incendiary_devices=mission.incendiary_devices,
            incendiary_devices_type=mission.incendiary_devices_type,
            incendiary_devices_weight_pounds=mission.incendiary_devices_weight_pounds,
            incendiary_devices_weight_tons=mission.incendiary_devices_weight_tons,
            fragmentation_devices=mission.fragmentation_devices,
            fragmentation_devices_type=mission.fragmentation_devices_type,
            fragmentation_devices_weight_pounds=mission.fragmentation_devices_weight_pounds,
            fragmentation_devices_weight_tons=mission.fragmentation_devices_weight_tons,
            total_weight_pounds=mission.total_weight_pounds,
            total_weight_tons=mission.total_weight_tons,
            time_over_target=mission.time_over_target,
            bomb_damage_assessment=mission.bomb_damage_assessment,
            source_id=mission.source_id
        )
        print('created new_mission')
        db.session.add(new_mission)
        print('added new_mission successfully')

        new_country = Country(
            name=mission.target_country,
        )
        db.session.add(new_country)

        new_city = City(
            name=mission.target_city,
        )
        db.session.add(new_city)

        new_coordinates = Coordinate(
            latitude=mission.target_latitude,
            longitude=mission.target_longitude,
        )
        db.session.add(new_coordinates)

        new_target = Target(
            country_id=counter,
            city_id=counter,
            coordinate_id=counter,
            target_type=mission.target_type,
            industry=mission.target_industry,
            priority=mission.target_priority,
        )
        db.session.add(new_target)

        counter += 1
    db.session.commit()
    print(f'finished normalizing data successfully! rows: {counter}')