import random
import datetime

class BankAccount:
    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.account_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])

class Bank:
    MAX_WITHDRAWAL_AMOUNT = 1000000  # Maximum withdrawal amount
    MAX_WITHDRAWAL_INSTANCE = 10000  # Maximum withdrawal amount per instance
    CURRENCY_SYMBOL = "R"  # Currency symbol

    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.blocked_cards = {}

    def create_account(self, account_holder, pin, initial_balance=0):
        account = BankAccount(account_holder, pin, initial_balance)
        self.accounts[account_holder] = account

    def authenticate_user(self, account_holder, pin):
        if account_holder in self.accounts and account_holder not in self.blocked_cards:
            account = self.accounts[account_holder]
            if account.pin == pin:
                return True
        return False

    def withdraw(self, account_holder, amount):
        if (
            account_holder in self.accounts
            and self.authenticate_user(account_holder, self.accounts[account_holder].pin)
            and amount % 10 == 0  # Check if amount is a multiple of 10
            and amount != 10  # Ensure amount is not equal to 10
            and amount <= self.MAX_WITHDRAWAL_INSTANCE  # Check if amount is within per-instance limit
            and amount <= self.MAX_WITHDRAWAL_AMOUNT  # Check if amount is within the overall limit
        ):
            if self.accounts[account_holder].balance >= amount:
                if amount <= self.MAX_WITHDRAWAL_INSTANCE:
                    self.accounts[account_holder].balance -= amount
                    return True
                else:
                    print("Amount exceeds per-instance withdrawal limit.")
                    print("Please contact your private banker for amounts exceeding", self.MAX_WITHDRAWAL_INSTANCE)
                    print("at 0800045454 (Name Surname).")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid withdrawal amount or authentication failed.")
        return False

    def deposit(self, account_holder, amount):
        if self.authenticate_user(account_holder, self.accounts[account_holder].pin):
            self.accounts[account_holder].balance += amount
            return True
        return False

    def check_balance(self, account_holder):
        if self.authenticate_user(account_holder, self.accounts[account_holder].pin):
            return self.accounts[account_holder].balance
        return None

    def print_account_details(self, account_holder):
        if account_holder in self.accounts:
            account = self.accounts[account_holder]
            print("Account Holder:", account.account_holder)
            print("Account Number:", account.account_number)
            print("Balance:", self.CURRENCY_SYMBOL, account.balance)  # Display currency symbol

    def print_slip(self, account_holder, amount):
        print("Printing slip for account holder:", account_holder)
        print("Transaction details:")
        print("Date:", datetime.datetime.now())
        self.print_account_details(account_holder)
        print("Amount withdrawn:", self.CURRENCY_SYMBOL, amount)  # Display currency symbol

    def block_card(self, account_holder):
        print("Too many incorrect attempts. Your card has been blocked.")
        print("Please contact your bank or call 0800005531 for help.")
        self.blocked_cards[account_holder] = True

    def is_card_blocked(self, account_holder):
        return account_holder in self.blocked_cards

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None
        self.pin_retry_count = 0

    def welcome_screen(self):
        print("Welcome to the", self.bank.name, "ATM")
        input("Press Enter to continue...")

    def enter_bank_details(self):
        account_holder = input("Enter your account holder name: ")
        if self.bank.is_card_blocked(account_holder):
            print("Your card is blocked. Please contact your bank or call 0800005531 for help.")
            return False

        while self.pin_retry_count < 3:
            pin = input("Enter your PIN: ")

            if self.bank.authenticate_user(account_holder, pin):
                self.current_user = account_holder
                self.pin_retry_count = 0
                print("Welcome,", account_holder + "!")
                return True
            else:
                self.pin_retry_count += 1
                print("Authentication failed. Please try again. Attempts left:", 3 - self.pin_retry_count)

        self.bank.block_card(account_holder)
        print("Your card has been blocked. Please contact your bank or call 0800005531 for help.")
        exit()

    def interactive_menu(self):
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Print Slip")
            print("5. Return Card")

            choice = input("\nEnter your choice (1-5): ")

            if choice == '1':
                amount = float(input("Enter withdrawal amount: "))
                if self.withdraw(amount):
                    self.print_slip_options(amount)
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                if self.deposit(amount):
                    self.thank_and_exit()
            elif choice == '3':
                self.check_balance()
                self.proceed_or_return_card()
            elif choice == '4':
                self.print_slip()
                self.print_slip_options()
            elif choice == '5':
                self.return_card()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def withdraw(self, amount):
        if self.bank.withdraw(self.current_user, amount):
            print("Withdrawal successful. Remaining balance:", self.bank.check_balance(self.current_user))
            return True
        else:
            print("Withdrawal failed. Invalid amount or insufficient funds.")
            return False

    def deposit(self, amount):
        if self.bank.deposit(self.current_user, amount):
            print("Deposit successful. New balance:", self.bank.check_balance(self.current_user))
            return True
        else:
            print("Deposit failed.")
            return False

    def check_balance(self):
        balance = self.bank.check_balance(self.current_user)
        if balance is not None:
            print("Your current balance:", self.bank.CURRENCY_SYMBOL, balance)  # Display currency symbol
        else:
            print("Error: Account not found.")

    def print_slip(self):
        self.bank.print_slip(self.current_user, 0.0)  # No amount needed for slip after withdrawal

    def print_slip_options(self, amount):
        while True:
            choice = input("Do you want to:\n1. Print Slip\n2. End\nEnter your choice (1 or 2): ")
            if choice == '1':
                self.print_slip_and_exit(amount)
            elif choice == '2':
                self.thank_and_exit()
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def print_slip_and_exit(self, amount):
        self.bank.print_slip(self.current_user, amount)
        print("Thank you for using the", self.bank.name, "ATM. Have a great day!")
        exit()

    def thank_and_exit(self):
        print("Thank you for using the", self.bank.name, "ATM. Have a great day!")
        exit()

    def proceed_or_return_card(self):
        while True:
            choice = input("Do you want to:\n1. Proceed\n2. Return Card\nEnter your choice (1 or 2): ")
            if choice == '1':
                break
            elif choice == '2':
                self.return_card()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def return_card(self):
        self.current_user = None
        self.pin_retry_count = 0
        print("Card returned. Thank you for using the", self.bank.name, "ATM.")
        exit()

# Example usage:
discovery_bank = Bank("Discovery Private Bank")
discovery_bank.create_account("MJ", "1234", 125000000)

woolies_bank = Bank("Woolies Global Bank")
woolies_bank.create_account("Bongs Mkhize", "5678", 75000)

banks = {"Discovery Private Bank": discovery_bank, "Woolies Global Bank": woolies_bank}

while True:
    bank_name = input("Enter the bank name (Discovery Private Bank or Woolies Global Bank): ")
    if bank_name in banks:
        selected_bank = banks[bank_name]
        break
    else:
        print("Invalid bank name. Please enter Discovery Private Bank or Woolies Global Bank.")

selected_atm = ATM(selected_bank)
selected_atm.welcome_screen()

while not selected_atm.enter_bank_details():
    pass  # Keep asking for bank details until successful authentication

selected_atm.interactive_menu()