from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return f"{self.name} is flying"

class SwimmingBird(Bird):
    def move(self):
        return f"{self.name} is swimming"

class Penguin(SwimmingBird):
    def make_sound(self):
        return "Honk honk"

class Sparrow(FlyingBird):
    def make_sound(self):
        return "Chirp chirp"

class Ostrich(Bird):
    def make_sound(self):
        return "Booming sound"

    def move(self):
        return f"{self.name} is running"

# Example usage:

penguin = Penguin("Penguin")
sparrow = Sparrow("Sparrow")
ostrich = Ostrich("Ostrich")

print(penguin.make_sound())  # Output: Honk honk
print(penguin.move())       # Output: Penguin is swimming

print(sparrow.make_sound())  # Output: Chirp chirp
print(sparrow.move())        # Output: Sparrow is flying

print(ostrich.make_sound())  # Output: Booming sound
print(ostrich.move())        # Output: Ostrich is running
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return f"{self.name} is flying"

class SwimmingBird(Bird):
    def move(self):
        return f"{self.name} is swimming"

class Penguin(SwimmingBird):
    def make_sound(self):
        return "Honk honk"

class Sparrow(FlyingBird):
    def make_sound(self):
        return "Chirp chirp"

class Ostrich(Bird):
    def make_sound(self):
        return "Booming sound"

    def move(self):
        return f"{self.name} is running"

# Example usage:

penguin = Penguin("Penguin")
sparrow = Sparrow("Sparrow")
ostrich = Ostrich("Ostrich")

print(penguin.make_sound())  # Output: Honk honk
print(penguin.move())       # Output: Penguin is swimming

print(sparrow.make_sound())  # Output: Chirp chirp
print(sparrow.move())        # Output: Sparrow is flying

print(ostrich.make_sound())  # Output: Booming sound
print(ostrich.move())        # Output: Ostrich is running
