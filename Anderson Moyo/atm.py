class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.pin_attempts = 0

    def input_details(self):
        print("Welcome to Capitec Bank self-service bot. Please create a new account to begin.")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.gender = input("Enter gender: ")
        self.create_pin()


    
    def create_pin(self):
        self.pin = input("Create a 4-digit PIN: ")
 # Abstraction: The details of how the PIN verification works are abstracted within the User class, 
 # providing a clean interface for PIN handling without revealing the internal implementation.
    def verify_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN!")
            self.pin_attempts += 1
            if self.pin_attempts == 3:
                print("Too many incorrect attempts. Terminating program.")
                exit()
            return False
#  Polymorphism: The show_details method is polymorphic in the sense that it is defined in both the User and Bank classes,
# but it behaves differently based on the context.
    def show_details(self):
        print("Personal Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
    
    def change_pin(self):
        new_pin = input("Enter your current PIN: ")
        if self.verify_pin(new_pin):
            self.pin = input("Enter a new 4-digit PIN: ")
            print("PIN has been successfully changed.")


class Bank(User):
    # Encapsulation: The use of classes to encapsulate related data (attributes) and behavior (methods) within the User and Bank classes.
    # Inheritance: The Bank class inherits from the User class, representing an "is-a" relationship, where a bank account "is-a" user with additional features.
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated: R", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds | Balance Available: R", self.balance)
        else:
            self.balance -= amount
            print("Account balance has been updated: R", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance: R", self.balance)


def show_options():
    print("\n===== Select an action =====")
    print("1. Show user details")
    print("2. Deposit")
    print("3. Show user balance")
    print("4. Withdraw")
    print("5. Change PIN")
    print("6. Exit")
    print("============================")


user = Bank("John", 20, "Male")
user.input_details()

while True:
    entered_pin = input("Enter your PIN: ")
    if user.verify_pin(entered_pin):
        break

while True:
    show_options()
    user_input = input("Enter your choice: ")

    if user_input == "1":
        user.show_details()

    elif user_input == "2":
        amount = int(input("Enter the amount to deposit: "))
        user.deposit(amount)

    elif user_input == "3":
        user.view_balance()

    elif user_input == "4":
        amount = int(input("Enter the amount to withdraw: "))
        user.withdraw(amount)
    elif user_input == "5":
        user.change_pin()

    elif user_input == "6":
        print("Exiting program.")
        exit()

    else:
        print("Invalid choice. Please choose a valid option.")

