# Exercise 3: Liskov Substitution Principle (LSP)
# Scenario: Create a system for a zoo that keeps track of different types of birds and their behaviors, such as flying and swimming.
# Task: Ensure that subclasses of the `Bird` class can be substituted without affecting the system's behavior. Consider how to handle birds that cannot fly.

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return True

    def swim(self):
        return True


class Duck(Bird):
    def fly(self):
        return True


class Goose(Bird):
    def fly(self):
        return True


class Penguin(Bird):
    def fly(self):
        return False


def main():
    birds = [Duck("Duck"), Goose("Goose"), Penguin("Penguin")]

    for bird in birds:
        print(bird.name, bird.fly(), bird.swim())


if __name__ == "__main__":
    main()

