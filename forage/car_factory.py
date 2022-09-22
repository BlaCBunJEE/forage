from forage.battery.Nubbin_battery import Nubbin
from forage.battery.Spindler_battery import Spindler
from forage.tyre.carrigan_tyre import Carrigan
from forage.tyre.octoprime_tyre import Octoprime
from forage.engine.willoughby_engine import WilloughbyEngine
from forage.engine.capulet_engine import CapuletEngine
from forage.engine.sternman_engine import SternmanEngine
from forage.car import Car


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,
                        tyre_wear_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Carrigan(tyre_wear_sensor)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on,
                          tyre_wear_sensor):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tyre = Octoprime(tyre_wear_sensor)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,
                        tyre_wear_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Carrigan(tyre_wear_sensor)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,
                         tyre_wear_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Octoprime(tyre_wear_sensor)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,
                      tyre_wear_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Octoprime(tyre_wear_sensor)
        car = Car(engine, battery, tyre)
        return car
