class ElectricityMeter:
    def __init__(self, initial_units):
        self.unit_balance = initial_units

    def upload_voucher(self, voucher_code):
        try:
            voucher_value = int(voucher_code)
            if len(str(voucher_value)) == 10:
                self.unit_balance += voucher_value / 2
                print("Voucher successfully uploaded.")
            else:
                print("Invalid voucher code. Please enter a 10-digit code.")
        except ValueError:
            print("Invalid voucher code. Please enter a numeric 10-digit code.")

    def display_units(self):
        print(f"Current unit balance: {self.unit_balance} units")


# Get initial unit balance from the user
initial_balance = int(input("Enter the initial unit balance: "))
meter = ElectricityMeter(initial_units=initial_balance)

# Interactive loop
while True:
    print("\nOptions:")
    print("1. Display units")
    print("2. Upload voucher")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        meter.display_units()
    elif choice == "2":
        voucher_code = input("Enter the 10-digit voucher code: ")
        meter.upload_voucher(voucher_code)
    elif choice == "3":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
