class Employee:

    def __init__(self, name :str, id_number:str, department:str):
        self.__name = name
        self.__id_number= id_number
        self.__department = department
        

    def display_details(self):
        return f"Employee: {self.__name}, ID: {self.__id_number}, Department: {self.__department}"



class Manager(Employee):
    # Manager is a subclass of Employee
    def __init__(self, name, id_number, department, managed_department):
        super().__init__(name, id_number, department)
        self.__managed_department = managed_department
 
    def display_details(self):
        # Overriding the method to add managed department
        basic_details = super().display_details()
        return f"{basic_details}, Managed Department: {self.__managed_department}"
    
    def display_details(self, details: str):
        return details
def employee_summary(employee):
        print(employee.display_details())

Sifiso = Employee("Sifiso", "9908056100399", "IT")
Thenjiwe = Manager("Thenjiwe Kubheka","970906","Stats","IT")

employee_summary(Sifiso)
employee_summary(Thenjiwe)




