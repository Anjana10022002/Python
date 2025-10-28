class vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate
    def display_details():
        return f"Vehicle id: {self.vehicle_id}, base rate_ {self.baseRate}"
    def rental_charge():
        return 0.0
    
    class car(vehicle):
        def rental_charges(self, num_seats):
            daily_rental = self.base_rate + self.num_seats
            return daily_rental
        
    class