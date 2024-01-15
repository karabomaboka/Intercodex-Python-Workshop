# Product interface
class Product:
    def produce(self):
        pass

# Concrete products
class ProductA(Product):
    def produce(self):
        print("Producing Product A")

class ProductB(Product):
    def produce(self):
        print("Producing Product B")

# Creator (Factory) interface
class Factory:
    def create_product(self):
        pass

# Concrete creators (Factories)
class FactoryA(Factory):
    def create_product(self):
        return ProductA()

class FactoryB(Factory):
    def create_product(self):
        return ProductB()

# Client code
class FactoryManagementSoftware:
    def __init__(self, factory):
        self.factory = factory

    def manage_production(self):
        product = self.factory.create_product()
        product.produce()

# Usage example
factory_a = FactoryA()
factory_b = FactoryB()

software_a = FactoryManagementSoftware(factory_a)
software_a.manage_production()

software_b = FactoryManagementSoftware(factory_b)
software_b.manage_production()