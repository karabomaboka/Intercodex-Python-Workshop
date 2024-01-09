class Product:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def name(self)->str:
        return self.__name
    
    def price(self)->float:
        return self.__price
    
    def quantity(self)->int:
        return self.__quantity

def update_quntity(self,  new_quantity : int)->None:
    self.__quantity = new_quantity

Milk = Product("Amasi", 1.00, 10)
Laptop = Product("Lenovo", 20.00, 20)

print(Milk.name())
print(Laptop.price())

Milk.update_quntity(new_quantity = 5)
print(Milk.quantity())


