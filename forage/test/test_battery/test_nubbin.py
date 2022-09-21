import unittest
from datetime import date
from forage.battery.Nubbin_battery import Nubbin


class TestNubbin(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
