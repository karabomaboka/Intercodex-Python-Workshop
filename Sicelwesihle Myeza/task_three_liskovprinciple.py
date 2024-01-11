# Exercise 3: Liskov Substitution Principle (LSP)
# Scenario: Create a system for a zoo that keeps track of different types of birds and their behaviors, such as flying and swimming.
# Task: Ensure that subclasses of the `Bird` class can be substituted without affecting the system's behavior. Consider how to handle birds that cannot fly.

# Your implementation here
class Bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the sound each bird makes

    def move(self):
        pass  # Placeholder for the movement behavior

class FlyingBird(Bird):
    def fly(self):
        print(f"{self.name} is flying")

class SwimmingBird(Bird):
    def swim(self):
        print(f"{self.name} is swimming")

class Sparrow(FlyingBird):
    def make_sound(self):
        print("Chirp chirp!")

class Penguin(SwimmingBird):
    def make_sound(self):
        print("Honk honk!")

# Zoo class to manage birds
class Zoo:
    def __init__(self):
        self.birds = []

    def add_bird(self, bird):
        self.birds.append(bird)

    def perform_activities(self):
        for bird in self.birds:
            bird.make_sound()
            bird.move()

# Example usage
sparrow = Sparrow("Sparrow1")
penguin = Penguin("Penguin1")

zoo = Zoo()
zoo.add_bird(sparrow)
zoo.add_bird(penguin)
zoo.perform_activities()
