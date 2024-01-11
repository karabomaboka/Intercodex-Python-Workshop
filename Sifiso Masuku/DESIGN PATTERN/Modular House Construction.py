class House:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def __str__(self):
        return f"House with modules: {', '.join(self.modules)}"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.add_module("Foundation")

    def build_walls(self):
        self.house.add_module("Walls")

    def build_roof(self):
        self.house.add_module("Roof")

    def build_interior(self):
        self.house.add_module("Interior")

    def get_house(self):
        return self.house


# Usage example
builder = HouseBuilder()
builder.build_foundation()
builder.build_walls()
builder.build_roof()
builder.build_interior()

house = builder.get_house()
print(house)  # Output: House with modules: Foundation, Walls, Roof, Interior