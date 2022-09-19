from abc import ABC

from forage.engine.car_engine import LyftEngine


class WilloughbyEngine(LyftEngine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        else:
            return False
