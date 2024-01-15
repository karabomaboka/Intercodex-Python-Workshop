class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None
        self.notifications = []

    def authenticate(self, account_number, entered_pin):
        account = self.bank.get_account(account_number)
        if account and entered_pin == account.pin:
            self.current_account = account
            return True
        else:
            return False

    def check_balance(self):
        if self.current_account:
            return f"Account Number: {self.current_account.account_number}\nBalance: R{self.current_account.balance}"
        else:
            return "Please authenticate first."

    def deposit(self, amount, target_account_number):
        if self.current_account:
            target_account = self.bank.get_account(target_account_number)
            if target_account:
                target_account.balance += amount
                notification = f"Deposited R{amount} into account {target_account_number}. New balance: R{target_account.balance}"
                self.notifications.append(notification)
                return notification
            else:
                return f"Target account {target_account_number} not found."
        else:
            return "Please authenticate first."

    def withdraw(self, amount):
        if self.current_account:
            if amount > 0 and amount <= self.current_account.balance:
                self.current_account.balance -= amount
                notification = f"Withdrew R{amount}. New balance: R{self.current_account.balance}"
                self.notifications.append(notification)
                return notification
            elif amount > self.current_account.balance:
                return "Insufficient funds."
            else:
                return "Invalid withdrawal amount."
        else:
            return "Please authenticate first."

    def get_notifications(self):
        return self.notifications

def main():
    bank = Bank()

    # Adding sample accounts
    account1 = BankAccount(account_number="123456", pin="1234", balance=1000)
    account2 = BankAccount(account_number="789012", pin="5678", balance=500)
    bank.add_account(account1)
    bank.add_account(account2)

    atm = ATM(bank)

    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if atm.authenticate(account_number, pin):
        print("Authentication successful. Welcome to the ATM!")
    else:
        print("Authentication failed. Exiting.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money into Another Account")
        print("3. Withdraw Money")
        print("4. View Notifications")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            target_account_number = input("Enter the target account number for deposit: ")
            amount = float(input("Enter the deposit amount: R"))
            print(atm.deposit(amount, target_account_number))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: R"))
            print(atm.withdraw(amount))
        elif choice == "4":
            notifications = atm.get_notifications()
            if notifications:
                print("\nBank Activity Notifications:")
                for notification in notifications:
                    print(notification)
            else:
                print("No notifications.")
        elif choice == "5":
            print("Exiting the ATM. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
