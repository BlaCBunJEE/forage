from abc import ABC, abstractmethod
from serviceable import Serviceable
from battery.car_battery import LyftBattery
from tyre.car_tyre import LyftTyre
from engine.car_engine import LyftEngine


class Car(Serviceable, ABC):
    def __init__(self):
        self.car_tyre = LyftTyre()
        self.car_battery = LyftBattery()
        self.car_engine = LyftEngine()

    @abstractmethod
    def needs_service(self):
        pass

    @abstractmethod
    def tyre_needs_service(self):
        pass
