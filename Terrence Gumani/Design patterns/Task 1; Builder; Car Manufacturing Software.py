class Car:
    def __init__(self):
        self.model = None
        self.colour = None
        self.engine_type = None
        self.accessories = []
        
    def __str__(self):
        return f"{self.colour}, {self.model} with {self.engine_type} engine type with the following accessories: {self.accessories}"
        
#Abstract Car builder
class Car_Builder:
    def __init__(self) -> None:
        self.car = Car()
    
    def build_model(self):
        pass
    
    def build_colour(self):
        pass
    
    def build_engine_type(self):
        pass
    
    def build_accessories(type):
        pass
    
#Concrete builders

class SUV_builder(Car_Builder):
    def build_model(self):
        self.car.model = "SUV"
        
    def build_colour(self):
        self.car.colour = "X Colour"
        
    def build_engine_type(self):
        self.car.engine_type = "3000 CC"
        
    def build_accessories(self):
        self.car.accessories = ["Wifi", "X-Box", "Apple play"]
        
class Cabriolet_builder(Car_Builder):
    def build_model(self):
        self.car.model = "Cabriolet"
        
    def build_colour(self):
        self.car.colour = "Y Colour"
        
    def build_engine_type(self):
        self.car.engine_type = "2000 CC"
        
    def build_accessories(self):
         self.car.accessories = ["TFSI", "Seat Warmers", "Child Lock"]
         
class Sedan_builder(Car_Builder):
    def build_model(self):
        self.car.model = "Sedan"
        
    def build_colour(self):
        self.car.colour = "Z Colour"
        
    def build_engine_type(self):
        self.car.engine_type = "8000 CC"
        
    def build_accessories(self):
        self.car.accessories = ["4WD", "DSG", "TV", "Android Play"]

# Car Director
class Car_Director:
    def construct(self, builder):
        builder.build_model()
        builder.build_colour()
        builder.build_engine_type()
        builder.build_accessories()
        return builder.car
    
# Client Code
director = Car_Director()

suv_builder = SUV_builder()
cabriolet_builder = Cabriolet_builder()
sedan_builder = Sedan_builder()

suv_car = director.construct(suv_builder)
cabriolet_car =director.construct(cabriolet_builder)
sedan_car = director.construct(sedan_builder)

print(suv_car) 
print(cabriolet_car)
print(sedan_car)   
