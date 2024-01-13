from abc import ABC, abstractmethod

# Part 1: Define an abstract base class for birds
class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Part 2: Implement concrete classes for flying and non-flying birds
class SkyDweller(Bird):
    def make_sound(self):
        print(f"{self.name} makes a sound")

    def fly(self):
        print(f"{self.name} gracefully soars through the sky")

class WaterAdmirer(Bird):
    def make_sound(self):
        print(f"{self.name} makes a sound")

    def swim(self):
        print(f"{self.name} enjoys swimming in the clear waters")

# Part 3: Extend the design for unique bird behaviors
class FlightlessBird(Bird):
    def make_sound(self):
        print(f"{self.name} emits a distinctive call")

class DivingBird(WaterAdmirer):
    def dive(self):
        print(f"{self.name} dives into the water with precision")

# Example Usage:

# Create instances of different birds
albatross = SkyDweller("Albatross")
penguin = DivingBird("Penguin")
ostrich = FlightlessBird("Ostrich")

# Use the birds in a generic way
birds = [albatross, penguin, ostrich]

for bird in birds:
    bird.make_sound()
    if isinstance(bird, SkyDweller):
        bird.fly()
    elif isinstance(bird, WaterAdmirer):
        bird.swim()
        if isinstance(bird, DivingBird):
            bird.dive()
