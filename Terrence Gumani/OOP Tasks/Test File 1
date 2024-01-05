# Base class (parent class)
class Vehicle:
    def __init__(self, name: str, model: str, year: int, engine_size: str, colour: str):
        self._name = name
        self._model = model
        self._year = year
        self._engine_size = engine_size
        self._colour = colour
        self._is_running = False

    def get_name(self) -> str:
        return self._name

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_engine_size(self) -> str:
        return self._engine_size

    def get_colour(self) -> str:
        return self._colour

    def __str__(self) -> str:
        return f"Name: {self._name}, Model: {self._model}, Year: {self._year}, Engine Size: {self._engine_size}, Colour: {self._colour}"

# Subclass 1
class Car(Vehicle):
    def __init__(self, name: str, model: str, year: int, engine_size: str, colour: str, num_doors: int, country: str):
        super().__init__(name, model, year, engine_size, colour)
        self._num_doors = num_doors
        self._country = country

    def get_num_doors(self) -> int:
        return self._num_doors

    def __str__(self) -> str:
        return super().__str__() + f", Num Doors: {self._num_doors}, Country: {self._country}"


# Subclass 2
class Motorcycle(Vehicle):
    def __init__(self, name: str, model: str, year: int, engine_size: str, colour: str, has_sidecar: bool, bike_type: str):
        super().__init__(name, model, year, engine_size, colour)
        self._has_sidecar = has_sidecar
        self._bike_type = bike_type

    def get_has_sidecar(self) -> bool:
        return self._has_sidecar

    def get_bike_type(self) -> str:
        return self._bike_type

    def __str__(self) -> str:
        return super().__str__() + f", Has Sidecar: {self._has_sidecar}, Bike Type: {self._bike_type}"


# Instances of subclasses
car1 = Car("Toyota", "Camry", 2022, "2.5L", "white", 4, "Toyota")
car2 = Car("Bentley", "Flying Spur", 2023, "V8", "Black", 4, "Bentley")
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2022, "1200cc", "red", False, "Sport")
motorcycle2 = Motorcycle("Big Boy", "Two-Wheeler", 2022, "900cc", "blue", True, "Delivery")

# Printing the details of the instances
print("Car 1 Details:")
print(car1)

print("\nCar 2 Details:")
print(car2)

print("\nMotorcycle 1 Details:")
print(motorcycle1)

print("\nMotorcycle 2 Details:")
print(motorcycle2)


