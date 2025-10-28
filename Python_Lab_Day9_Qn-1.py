class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate
    def display_details():
        return f"Vehicle id: {self.vehicle_id}, base rate_ {self.baseRate}"
    def rental_charge():
        return 0.0
    
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self._num_seats = num_seats

    def rental_charges(self):
        daily_rental = self._base_rate + self._num_seats
        return daily_rental

    def display_details(self):
        return f"Vehicle id: {self._vehicle_id}, base rate: {self._base_rate}, number of seats: {self._num_seats}"

class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self._bike_type = bike_type
        self.bike_type = bike_type

    def rental_charges(self, bike_type, base_rate):
        daily_rental = self._base_rate * 0.5
        return daily_rental
    



