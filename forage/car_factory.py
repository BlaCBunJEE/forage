from forage.battery.Nubbin_battery import Nubbin
from forage.battery.Spindler_battery import Spindler
from forage.tyre.Bridgestone_tyre import Bridgestone
from forage.tyre.dunlop_tyre import Dunlop
from forage.engine.willoughby_engine import WilloughbyEngine
from forage.engine.capulet_engine import CapuletEngine
from forage.engine.sternman_engine import SternmanEngine
from forage.car import Car


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,
                        tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on,
                          tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_tyre_service_mileage)
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,
                        tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,
                         tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,
                      tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)
        car = Car(engine, battery, tyre)
        return car
