import unittest
import random
from forage.tyre.carrigan_tyre import Carrigan


class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_wear_sensor = [0.3, 0.6, 0.4, 0.9]
        # sensor_range = range(4)
        # for value in sensor_range:
        #     random_sensor_value = round(random.random(), 1)
        #     tyre_wear_sensor.append(random_sensor_value)
        tyre = Carrigan(tyre_wear_sensor)
        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_wear_sensor = [0.7, 0.3, 0.6, 0.6]
        # sensor_range = range(4)
        # for value in sensor_range:
        #     random_sensor_value = round(random.random(), 1)
        #     tyre_wear_sensor.append(random_sensor_value)
        tyre = Carrigan(tyre_wear_sensor)
        self.assertFalse(tyre.tyre_needs_service())


if __name__ == '__main__':
    unittest.main()
