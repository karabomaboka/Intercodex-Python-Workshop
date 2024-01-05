# Class representing Employee ID
class Employee:
    def __init__(self, emp_id:int, name:str):
        self.emp_id = emp_id
        self.name = name 
        
    def get_emp_id(self) -> int:
        return self.emp_id    
    def get_name(self) -> str:
        return self.name

    def __str__(self):
        return f"Employee {self.emp_id}:  {self.name}"

# Class representing a Student
class Student:
    def __init__(self, student_id:int, name:str):
        self.student_id = student_id
        self.name = name
        
    def get_student_id(self) -> int:
        return self.student_id
    def get_name(self) -> str:
        return self.name
        
    def __str__(self):
        return f"Student {self.student_id}: {self.name}"
    
# Class representing Team = aggregation of Employee and Student

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []
        
    def add_member(self, member):
        self.members.append(member)
        
    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print(f"{member} is not a memebr of {self.team_name}")
            
    def display_members(self):
        print(f"Members of Team '{self.team_name}':")
        for member in self.members:
            print(f"- {member}")
            
# Creating instances of Employee and Student
employee1 = Employee(1, "Koketso Mohale")
employee2 = Employee(2, "Saul Ngobese")

student1 = Student(101, "Akhile Mcimeli")
student2 = Student(102, "Terrence Gumani")

# Creating instances of Team and adding members
team1 = Team("Business Analysts Team")
team1.add_member(employee1)
team1.add_member(employee2)
team1.add_member(student1)

team2 = Team("Business Intelligence Team")
team2.add_member(student2)

# Displaying members of each team
team1.display_members()
print()  # Just for formatting

team2.display_members()
print()  # Just for formatting

# Removing a member from a team
team1.remove_member(employee1)

# Displaying members of the team after removal
team1.display_members()
              
    
    
   
      