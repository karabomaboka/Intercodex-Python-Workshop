from abc import ABC, abstractmethod

# Component - Vehicle
class Vehicle(ABC):
    @abstractmethod
    def get_info(self):
        pass

# Leaf - Car
class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def get_info(self):
        return f"Car - Model: {self.model}"

# Leaf - Truck
class Truck(Vehicle):
    def __init__(self, model):
        self.model = model

    def get_info(self):
        return f"Truck - Model: {self.model}"

# Leaf - Bus
class Bus(Vehicle):
    def __init__(self, model):
        self.model = model

    def get_info(self):
        return f"Bus - Model: {self.model}"

# Composite - Fleet
class Fleet(Vehicle):
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def get_info(self):
        fleet_info = ""
        for vehicle in self.vehicles:
            fleet_info += vehicle.get_info() + "\n"
        return fleet_info

# Example Usage
car1 = Car("Sedan 1")
car2 = Car("SUV 1")
truck1 = Truck("Cargo 1")
bus1 = Bus("Tourist 1")

fleet = Fleet()
fleet.add_vehicle(car1)
fleet.add_vehicle(car2)
fleet.add_vehicle(truck1)
fleet.add_vehicle(bus1)

print(fleet.get_info())
