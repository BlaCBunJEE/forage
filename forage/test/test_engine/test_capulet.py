import unittest
from forage.engine.capulet_engine import CapuletEngine


class TestCapulet(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
