from forage.tyre.car_tyre import LyftTyre
import random


class Carrigan(LyftTyre):
    def __init__(self, tyre_wear_sensor):
        self.tyre_wear_sensor = tyre_wear_sensor

    def tyre_needs_service(self):
        print(self.tyre_wear_sensor)
        for tyre in self.tyre_wear_sensor:
            if tyre >= 0.9:
                return True
        return False








