class BankAccount:
    def __init__(self, account_holder: str, pin: str, balance: float):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def withdraw(self, amount: float):
        if amount <= self.balance and amount > 10 and amount % 10 == 0:
            self.balance -= amount
            return f"Withdraw R{amount}. New Balance: R{self.balance}"
        else:
            return "Invalid withdrawal amount."

    def deposit(self, amount: float):
        self.balance += amount
        return f"Deposited R{amount}. New balance: R{self.balance}"

    def get_balance(self):
        return f"Current balance: R{self.balance}"

    def change_pin(self, current_pin, new_pin):
        if current_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect current PIN. PIN not changed."


class ATM:
    def __init__(self):
        self.accounts = {}
        self.max_attempts = 3
        self.attempts_counter = {}

    def create_account(self, account_holder, pin, balance):
        account = BankAccount(account_holder, pin, balance)
        self.accounts[pin] = account
        return f"Account Created for {account_holder}"

    def get_account(self, entered_pin):
        return self.accounts.get(entered_pin)

    def validate_pin(self, entered_pin):
        return entered_pin in self.accounts

    def welcome_user(self, account_holder):
        print(f"Welcome, {account_holder}")

    def show_options(self):
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balances")
        print("4. Change PIN")

    def perform_transaction(self, option, entered_pin):
        if option == "1":
            amount = float(input("Enter Amount: "))
            return self.withdraw(amount, entered_pin)
        elif option == "2":
            amount = float(input("Enter Amount: "))
            return self.deposit(amount, entered_pin)
        elif option == "3":
            return self.check_balance(entered_pin)
        elif option == "4":
            return self.change_pin(entered_pin)
        else:
            return "Invalid pick"

    def display_transaction_result(self, result):
        print(result)

    def run_atm(self):
        print("Welcome to the ATM")

        for _ in range(self.max_attempts):
            entered_pin = input("Please enter your pin: ")

            if self.validate_pin(entered_pin):
                account_holder = self.accounts[entered_pin].account_holder
                self.welcome_user(account_holder)

                self.attempts_counter[entered_pin] = 0

                while True:
                    self.show_options()
                    option = input("Enter the number of the transaction: ")
                    if option.lower() == "exit":
                        break

                    result = self.perform_transaction(option, entered_pin)
                    self.display_transaction_result(result)

                break
            else:
                self.attempts_counter[entered_pin] = self.attempts_counter.get(entered_pin, 0) + 1

                if self.attempts_counter[entered_pin] >= self.max_attempts:
                    print("Card blocked. Too many incorrect PIN attempts.")
                    return  # Exit the program if the card is blocked
                else:
                    print(f"Incorrect pin: Attempt {self.attempts_counter[entered_pin]} of {self.max_attempts}")

        print("Card blocked. Too many incorrect PIN attempts.")  # Print the message before breaking

    def check_balance(self, entered_pin):
        if self.validate_pin(entered_pin):
            return self.accounts[entered_pin].get_balance()
        else:
            return "Invalid transaction"


    def change_pin(self, entered_pin):
        if self.validate_pin(entered_pin):
            current_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")

            result = self.accounts[entered_pin].change_pin(current_pin, new_pin)
            return result
        else:
            return "Invalid transaction"

# Example
if __name__ == "__main__":
    atm = ATM()
    print(atm.create_account(account_holder="anderson", pin="0000", balance=1000))
    atm.run_atm()
