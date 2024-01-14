class ATM:
    def __init__(self,balance=0,pin=0000):
        self.__balance = balance
        self.pin = pin 

    def check_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount > self.__balance:
            return "Insufficient funds."
        else:
            self.__balance -= amount
            return f"Withdrawal succesful. Current balance:{self.__balance}"
    
    def deposit(self,amount):
        self.__balance += amount 
        return f"Deposit succesful. Current balance: {self.__balance}"
    
    def change_pin(self,new_pin):
        self.pin = new_pin
        return "Pin changed succesfully"
    

def main():
    atm = ATM(1000,1234)
    while True:
        attempts = 0
        print("Welcome to the ATM.")
        pin = int(input("Please enter your pin:"))
        while attempts < 3:

        
            if pin != atm.pin:
                attempts += 1
                if attempts >= 3:
                    print(f"Your account is blocked!")

                else:
                    print(f"Invalid transaction. You have {3 - attempts} attempts left")
                    pin = int(input("Please enter your pin:"))
                
                continue
            
            
            # reset back to 0 attempts 
            attempts = 0
            print("\nMenu")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change pin")
            print("5. Exit")

            option = int(input("\nEnter your choice: "))

            if option == 1:
                print(f"Current balance:{atm.check_balance()}")
    
            elif option == 2:
                amount = float(input("Enter the amount to withdraw: "))
                print(f"{atm.withdraw(amount)}")

            elif option == 3:
                amount = float(input("Enter the amount to deposit: "))
                print(f"{atm.deposit(amount)}")
    
            elif option == 4:
                new_pin = int(input("Enter your new pin: "))
                print(f"{atm.change_pin(new_pin)}")

            elif option == 5:
                print("Thank you for using the ATM machine.")
                break

            else:
                pass

if __name__ == "__main__":
    main()
