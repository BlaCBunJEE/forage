from datetime import datetime

from forage.car import Car


class Rorschach(Car):

    def __init__(self):
        super().__init__()
        self.last_service_date = None

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False

    def tyre_needs_service(self):
        return self.tyre_needs_service()
