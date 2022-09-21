import unittest
from forage.tyre.dunlop_tyre import Dunlop


class TestDunlop(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
