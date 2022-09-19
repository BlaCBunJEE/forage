from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, tyre, battery, engine):
        self.tyre = tyre
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        pass

    def tyre_needs_service(self):
        pass
