class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department

    def display_details(self):
        
        return f"Employee: {self.name}, ID: {self.id_number}, Department: {self.department}"

employee1 = Employee("Thenjiwe Khubeka", "123456", "Exec")


print(employee1.display_details())
