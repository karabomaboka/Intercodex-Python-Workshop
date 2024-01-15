from abc import ABC, abstractmethod

# Component (Abstract Vehicle)
class Vehicle(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Leaf (Concrete Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def get_details(self):
        return f"Car: {self.brand} {self.model}, Fuel Type: {self.fuel_type}"

# Leaf (Concrete Vehicle)
class Truck(Vehicle):
    def __init__(self, brand, model, payload_capacity):
        self.brand = brand
        self.model = model
        self.payload_capacity = payload_capacity

    def get_details(self):
        return f"Truck: {self.brand} {self.model}, Payload Capacity: {self.payload_capacity} tons"

# Composite (Group of Vehicles)
class VehicleGroup(Vehicle):
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def get_details(self):
        details = f"Vehicle Group: {self.name}\n"
        for vehicle in self.vehicles:
            details += vehicle.get_details() + "\n"
        return details

# Usage example
car1 = Car("Toyota", "Camry", "Petrol")
car2 = Car("Honda", "Accord", "Hybrid")
truck1 = Truck("Volvo", "FH16", 25)
truck2 = Truck("Mercedes-Benz", "Actros", 30)

vehicle_group = VehicleGroup("Fleet 1")
vehicle_group.add_vehicle(car1)
vehicle_group.add_vehicle(car2)
vehicle_group.add_vehicle(truck1)
vehicle_group.add_vehicle(truck2)

print(vehicle_group.get_details())