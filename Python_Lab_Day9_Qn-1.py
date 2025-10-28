class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate
    def display_details():
        return f"Vehicle id: {self.vehicle_id}, base rate_ {self.baseRate}"
    def rental_charge():
        return 0.0
    
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_rate):
        super().__init__(vehicle_id, base_rate, num_rate)
        self._num_rate = num_rate

    def rental_charges(self, num_seats, base_rate):
        daily_rental = self.base_rate + self.num_seats
        return daily_rental
        
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate, bike_type)
        self.bike_type = bike_type

    def rental_charges(self, bike_type, base_rate):
        daily_rental = self._base_rate * 0.5
        return daily_rental
    
    


