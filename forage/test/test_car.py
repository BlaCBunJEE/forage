import unittest
from datetime import datetime, date
from forage.car_factory import CarFactory
from forage.battery.Nubbin_battery import Nubbin
from forage.battery.Spindler_battery import Spindler
from forage.tyre.Bridgestone_tyre import Bridgestone
from forage.tyre.dunlop_tyre import Dunlop
from forage.engine.willoughby_engine import WilloughbyEngine
from forage.engine.capulet_engine import CapuletEngine
from forage.engine.sternman_engine import SternmanEngine


class TestCalliope(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 31000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 3)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 1)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_tyre_should_be_serviced(self):
        tyre_thread_wear = True
        current_tyre_mileage = 120000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_thread_wear = False
        current_tyre_mileage = 90000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertFalse(tyre.tyre_needs_service())



class TestPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 3)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 1)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_tyre_should_be_serviced(self):
        tyre_thread_wear = True
        current_tyre_mileage = 120000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_thread_wear = False
        current_tyre_mileage = 90000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertFalse(tyre.tyre_needs_service())



class TestGlissade(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 61000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 3)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 1)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Spindler(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_tyre_should_be_serviced(self):
        tyre_thread_wear = True
        current_tyre_mileage = 155000
        last_tyre_service_mileage = 0
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_thread_wear = False
        current_tyre_mileage = 145000
        last_tyre_service_mileage = 0
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertFalse(tyre.tyre_needs_service())


class TestRorshach(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 61000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 5)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Nubbin(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 3)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Nubbin(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_tyre_should_be_serviced(self):
        tyre_thread_wear = True
        current_tyre_mileage = 155000
        last_tyre_service_mileage = 0
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_thread_wear = False
        current_tyre_mileage = 145000
        last_tyre_service_mileage = 0
        tyre = Bridgestone(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertFalse(tyre.tyre_needs_service())


class TestThovex(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 31000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 5)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Nubbin(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today_date = date.today()
        previous_service_date = today_date.replace(year=today_date.year - 3)
        current_date = int(today_date.year)
        last_service_date = int(previous_service_date.year)
        battery = Nubbin(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_tyre_should_be_serviced(self):
        tyre_thread_wear = True
        current_tyre_mileage = 110000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertTrue(tyre.tyre_needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_thread_wear = False
        current_tyre_mileage = 99000
        last_tyre_service_mileage = 0
        tyre = Dunlop(tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage)

        self.assertFalse(tyre.tyre_needs_service())



if __name__ == '__main__':
    unittest.main()
