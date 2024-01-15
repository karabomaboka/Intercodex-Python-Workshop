# Product - House
class House:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def display_modules(self):
        print("House with the following modules:")
        for module in self.modules:
            print(f" - {module}")

# Builder Interface
class HouseBuilder:
    def build_walls(self):
        pass

    def build_doors(self):
        pass

    def build_windows(self):
        pass

    def get_house(self):
        pass

# Concrete Builder for Basic House
class BasicHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add_module("Basic Walls")

    def build_doors(self):
        self.house.add_module("Basic Doors")

    def build_windows(self):
        self.house.add_module("Basic Windows")

    def get_house(self):
        return self.house

# Concrete Builder for Luxury House
class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add_module("Luxury Walls")

    def build_doors(self):
        self.house.add_module("Luxury Doors")

    def build_windows(self):
        self.house.add_module("Luxury Windows")

    def get_house(self):
        return self.house

# Director
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()

# Example Usage
basic_builder = BasicHouseBuilder()
luxury_builder = LuxuryHouseBuilder()

director = HouseDirector(basic_builder)
director.construct_house()
basic_house = basic_builder.get_house()
basic_house.display_modules()

director = HouseDirector(luxury_builder)
director.construct_house()
luxury_house = luxury_builder.get_house()
luxury_house.display_modules()
