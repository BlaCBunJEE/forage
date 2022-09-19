from forage.tyre.car_tyre import LyftTyre


class Bridgestone(LyftTyre):
    def __init__(self, tyre_thread_wear, current_tyre_mileage, last_tyre_service_mileage):
        self.tyre_thread_wear = tyre_thread_wear
        self.current_tyre_mileage = current_tyre_mileage
        self.last_tyre_service_mileage = last_tyre_service_mileage

    def tyre_needs_service(self):
        if self.tyre_thread_wear == 'True' \
                or self.current_tyre_mileage - self.last_tyre_service_mileage > 150000:
            return 'Change car Tyres'
