class BankAccount:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.incorrect_pin_attempts = 0
        self.blocked = False

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.blocked:
            return "Account is blocked. Please contact customer support."
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def deposit(self, amount):
        if self.blocked:
            return "Account is blocked. Please contact customer support."
        self.balance += amount
        return amount

    def increment_incorrect_pin_attempts(self):
        self.incorrect_pin_attempts += 1
        if self.incorrect_pin_attempts >= 3:
            self.blocked = True

class ATM:
    def __init__(self, bank_accounts):
        self.bank_accounts = bank_accounts

    def authenticate(self, account_number, pin):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                if account.pin == pin:
                    account.incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
                    return account
                else:
                    account.increment_incorrect_pin_attempts()
                    return None
        return None

    def withdraw(self, account, amount):
        return account.withdraw(amount)

    def deposit(self, account, amount):
        return account.deposit(amount)

def main():
    # Create bank accounts
    bank_accounts = [
        BankAccount("123456789", "1234", 1000),
        BankAccount("987654321", "4321", 500)
    ]
    atm = ATM(bank_accounts)
    # Prompt user for account number and PIN
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    # Authenticate the user
    account = atm.authenticate(account_number, pin)
    if account:
        print("Authentication successful")
        while True:
            # Prompt user for operation choice
            print("Choose an operation:")
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                balance = account.check_balance()
                print("Balance:", balance)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                withdrawal = atm.withdraw(account, amount)
                print("Withdrawal:", withdrawal)
                print("Balance:", account.check_balance())
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                deposit = atm.deposit(account, amount)
                print("Deposit:", deposit)
                print("Balance:", account.check_balance())
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid account number or PIN")

if __name__ == "__main__":
    main()