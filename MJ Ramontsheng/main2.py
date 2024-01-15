# Define the base Car interface
class Car:
    def assemble(self):
        pass

# Concrete implementations of different types of cars
class Sedan(Car):
    def assemble(self):
        return "Sedan"

class SUV(Car):
    def assemble(self):
        return "SUV"

class Hatchback(Car):
    def assemble(self):
        return "Hatchback"

# Decorator classes for customizations
class CarDecorator(Car):
    def __init__(self, car):
        self._car = car

    def assemble(self):
        return self._car.assemble()

class ColorDecorator(CarDecorator):
    def __init__(self, car, color):
        super().__init__(car)
        self._color = color

    def assemble(self):
        return f"{super().assemble()} - Color: {self._color}"

class EngineDecorator(CarDecorator):
    def __init__(self, car, engine_type):
        super().__init__(car)
        self._engine_type = engine_type

    def assemble(self):
        return f"{super().assemble()} - Engine: {self._engine_type}"

class AccessoryDecorator(CarDecorator):
    def __init__(self, car, accessory):
        super().__init__(car)
        self._accessory = accessory

    def assemble(self):
        return f"{super().assemble()} - Accessory: {self._accessory}"

# Client code
def main():
    # Create a base Sedan
    sedan = Sedan()

    # Add customizations
    customized_sedan = ColorDecorator(EngineDecorator(sedan, "V6"), "Blue")
    print(customized_sedan.assemble())

    # Create a base SUV
    suv = SUV()

    # Add customizations
    customized_suv = EngineDecorator(AccessoryDecorator(suv, "Roof Rack"), "V8")
    print(customized_suv.assemble())

if __name__ == "__main__":
    main()
