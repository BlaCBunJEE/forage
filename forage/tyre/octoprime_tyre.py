from forage.tyre.car_tyre import LyftTyre
import random


class Octoprime(LyftTyre):
    def __init__(self, tyre_wear_sensor):
        self.tyre_wear_sensor = tyre_wear_sensor


    def tyre_needs_service(self):
        return sum(self.tyre_wear_sensor) >= 3.0




