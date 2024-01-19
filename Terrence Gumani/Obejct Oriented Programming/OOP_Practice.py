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

class Developer(Employee):
    pass
    
    # @classmethod is a decorator used to define a class method. 
    # A class method is a method that is bound to the class and not the instance of the class. 
    # It takes the class itself as its first parameter, conventionally named cls. 
    # @classmethod
    # def set_raise_amount(cls, amount):
    #     cls.raise_amount = amount

dev_1 = Developer('Terry', 'Guamni', 100000)
dev_2 = Developer('Nqobile', 'Gumani', 100200)

print(help(Developer))

# Employee.set_raise_amount(1.05)

# print(emp_2.raise_amount)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
