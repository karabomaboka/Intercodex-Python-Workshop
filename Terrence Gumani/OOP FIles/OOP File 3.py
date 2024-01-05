class Employee:
    
    def __init__(self, name, id_number, department):
        self.__name = name
        self.__id_number = id_number
        self.__department = department

    def display_details(self):
        
        return f"Employee: {self.__name}, ID: {self.__id_number}, Department: {self.__department}"

Thenjiwe = Employee("Thenjiwe Khubeka", "123456", "Exec")


class Manager(Employee):
    # Manager is a subclass of Employee
    def __init__(self, name, id_number, department, managed_department):
        super().__init__(name, id_number, department)
        self.__managed_department = managed_department
 
    def display_details(self):
        # Overriding the method to add managed department
        basic_details = super().display_details()
        return f"{basic_details}, Managed Department: {self.__managed_department}"
    
Kgothatso = Manager("Kgothatso Matlala", "023785", "Group:Tech", "IT")
    
print(Thenjiwe.display_details())    
print(Kgothatso.display_details())