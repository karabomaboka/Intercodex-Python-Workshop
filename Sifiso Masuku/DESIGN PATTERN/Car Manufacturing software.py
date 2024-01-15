class Car:
    def __init__(self, model, color, engine_type):
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.accessories = []

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def __str__(self):
        return f"Car: {self.model}, Color: {self.color}, Engine Type: {self.engine_type}, Accessories: {', '.join(self.accessories)}"


class CarFactory:
    def create_car(self, model, color, engine_type):
        car = self.create_base_car(model, color, engine_type)
        self.add_customizations(car)
        return car

    def create_base_car(self, model, color, engine_type):
        return Car(model, color, engine_type)

    def add_customizations(self, car):
        pass


class SedanCarFactory(CarFactory):
    def add_customizations(self, car):
        car.add_accessory("Leather Seats")
        car.add_accessory("Sunroof")


class SUVCarFactory(CarFactory):
    def add_customizations(self, car):
        car.add_accessory("Roof Rack")
        car.add_accessory("All-Wheel Drive")


class HatchbackCarFactory(CarFactory):
    def add_customizations(self, car):
        car.add_accessory("Rear Spoiler")
        car.add_accessory("Fog Lights")


def main():
    sedan_factory = SedanCarFactory()
    sedan = sedan_factory.create_car("Sedan", "Red", "Petrol")
    print(sedan)

    suv_factory = SUVCarFactory()
    suv = suv_factory.create_car("SUV", "Blue", "Diesel")
    print(suv)

    hatchback_factory = HatchbackCarFactory()
    hatchback = hatchback_factory.create_car("Hatchback", "Green", "Electric")
    print(hatchback)


if __name__ == "__main__":
    main()