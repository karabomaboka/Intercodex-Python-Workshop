class Employee:
    
    def __init__(self, name, id_number, department):
        self.__name = name
        self.__id_number = id_number
        self.__department = department

    def display_details(self):
        
        return f"Employee: {self.__name}, ID: {self.__id_number}, Department: {self.__department}"

Thenjiwe = Employee("Thenjiwe Khubeka", "123456", "Exec")

print(Thenjiwe.display_details())
