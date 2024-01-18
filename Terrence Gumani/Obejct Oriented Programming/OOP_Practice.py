#Python Object Oriented Programming
class Employee:
    
    raise_amount = 1.10
    number_of_emps = 0
    
    def __init__(self, name:str, surname:str, salary:float):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + '.' + surname + '@company.co.za'

        Employee.number_of_emps += 1
        
    def fullname(self):
        return '{} {} {} {}' .format(self.name, self.surname, self.salary, self.email)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

emp_1 = Employee('Terry', 'Guamni', 100000)
emp_2 = Employee('Nqobile', 'Gumani', 100200)


