import random

class PrepaidElectricityMeter:
    def __init__(self, meter_id, initial_credit=0.0, rate_per_kwh=0.15):
        self.meter_id = meter_id
        self.credit = initial_credit
        self.rate_per_kwh = rate_per_kwh

    def add_credit(self, voucher_code):
        # Validate voucher code (for simplicity, checking if it's 10 digits)
        if voucher_code.isdigit() and len(voucher_code) == 10:
            # Add a random credit amount (e.g., between R10 and R100)
            credit_amount = round(random.uniform(10.0, 100.0), 2)
            self.credit += credit_amount

            print(f"Recharge successful! Added R{credit_amount:.2f} using voucher code: {voucher_code}")
            print(f"Remaining credit: R{self.credit:.2f}")
        else:
            print("Invalid voucher code. Please enter a 10-digit numerical code.")

    def record_consumption(self, kwh):
        cost = kwh * self.rate_per_kwh
        if cost <= self.credit:
            self.credit -= cost
            print(f"Consumption recorded: {kwh:.2f} kWh. Remaining credit: R{self.credit:.2f}")
        else:
            print("Insufficient credit. Please recharge.")

    def get_meter_info(self):
        return f"Meter ID: {self.meter_id}\nCurrent Credit: R{self.credit:.2f}\nRate per kWh: R{self.rate_per_kwh:.2f}"

# Example Usage:
prepaid_meter = PrepaidElectricityMeter("PEM456", initial_credit=0.0, rate_per_kwh=0.15)

# User enters voucher code
user_voucher_code = input("Enter the 10-digit voucher code: ")

# Add credit using the user-entered voucher code
prepaid_meter.add_credit(user_voucher_code)

# Record consumption readings
consumption = float(input("Enter kWh consumed: "))
prepaid_meter.record_consumption(consumption)

# Get information about the meter
print(prepaid_meter.get_meter_info())

# Record consumption readings
consumption = float(input("Enter kWh consumed: "))
prepaid_meter.record_consumption(consumption)

# Get final information about the meter
print(prepaid_meter.get_meter_info())

