class Engine:
    def __init__(self, size: float):
        self.size = size
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"Engine started. Size: {self.size}L")

    def stop(self):
        self.is_running = False
        print("Engine stopped")


class Wheels:
    def __init__(self, count: int):
        self.count = count

    def rotate(self):
        print(f"Wheels are rotating. Number of wheels: {self.count}")


class Drivetrain:
    def __init__(self, number_of_gears: int):
        self.number_of_gears = number_of_gears
        self.current_gear = 1

    def shift_gear(self, new_gear: int):
        if 1 <= new_gear <= self.number_of_gears:
            self.current_gear = new_gear
            print(f"Shifted to gear {new_gear}")
        else:
            print(f"Invalid gear. Must be between 1 and {self.number_of_gears}")

    def get_current_gear(self) -> int:
        return self.current_gear


class Car:
    def __init__(self, engine: Engine, wheels: Wheels, drivetrain: Drivetrain, make: str, model: str, year: int, colour: str):
        self.engine = engine
        self.wheels = wheels
        self.drivetrain = drivetrain
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def start(self):
        self.engine.start()
        print(f"The {self.year} {self.make} {self.model} is ready to go!")

    def stop(self):
        self.engine.stop()
        print(f"The {self.year} {self.make} {self.model} has come to a stop.")

    def drive(self, speed: int):
        if self.engine.is_running:
            print(f"The {self.year} {self.make} {self.model} is moving at {speed} km/h.")
        else:
            print(f"Start the engine first before driving the {self.year} {self.make} {self.model}.")

    def change_gear(self, new_gear: int):
        self.drivetrain.shift_gear(new_gear)
        print(f"Changed to gear {new_gear}")

    def show_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}, Colour: {self.colour}")

# Creating objects for Engine, Wheels, and Drivetrain
car_engine = Engine(size=2.5)
car_wheels = Wheels(count=4)
car_drivetrain = Drivetrain(number_of_gears=6)

my_car = Car(engine=car_engine, wheels=car_wheels, drivetrain=car_drivetrain,
             make="Toyota", model="Camry", year=2022, colour="Blue")

# Using Car methods to start, stop, drive, and change gears
my_car.start()
my_car.drive(60)
my_car.change_gear(3)
my_car.drive(80)
my_car.stop()

# Displaying Car details
my_car.show_details()
