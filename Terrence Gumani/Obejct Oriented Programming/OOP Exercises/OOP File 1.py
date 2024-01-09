class Product: 
    def __init__(self, name: str, price: float, quantity: int): 
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price
    
    def get_name(self) -> int:
        return self._quantity
    
    def get_update_quantity(self, new_quantity:int) -> None:
        self._quantity = new_quantity

milk = Product(name='Amasi',price= 2.49,quantity= 98)
broccoli = Product(name='broccoli',price= 5.96,quantity= 98)
wors = Product(name='boerwors',price= 9.99,quantity= 1990)

print(wors.get_name())
print(wors.get_price())
milk.get_update_quantity(new_quantity=6)
