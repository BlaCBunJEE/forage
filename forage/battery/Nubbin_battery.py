from forage.battery.car_battery import LyftBattery


class Nubbin(LyftBattery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        if self.current_date - self.last_service_date > 4:
            return True
        else:
            return False
