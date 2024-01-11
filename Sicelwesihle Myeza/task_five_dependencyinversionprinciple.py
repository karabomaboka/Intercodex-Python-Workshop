# Exercise 5: Dependency Inversion Principle (DIP)
# Scenario: Imagine creating an e-commerce application that processes orders and payments. The payment process can be done through various methods (e.g., credit card, PayPal, bank transfer).
# Task: Develop the system in a way that the high-level order processing module is not dependent on the low-level payment modules. Think about how you would design the system to easily accommodate new payment methods in the future.

# Your implementation here
from abc import ABC, abstractmethod

# Define an abstraction for payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Implement concrete payment methods
class CreditCardPayment(PaymentMethod):
    def process_payment(self):
        print("Processing payment via Credit Card")

class PayPalPayment(PaymentMethod):
    def process_payment(self):
        print("Processing payment via PayPal")

class BankTransferPayment(PaymentMethod):
    def process_payment(self):
        print("Processing payment via Bank Transfer")

# High-level order processing module
class OrderProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_order(self):
        print("Processing the order")
        # Additional order processing logic goes here

        # Delegate payment processing to the injected payment method
        self.payment_method.process_payment()
        print("Order processed successfully!")

# Usage example
if __name__ == "__main__":
    
    credit_card_payment = CreditCardPayment()
    order_processor_credit_card = OrderProcessor(credit_card_payment)
    order_processor_credit_card.process_order()

    paypal_payment = PayPalPayment()
    order_processor_paypal = OrderProcessor(paypal_payment)
    order_processor_paypal.process_order()

   
    bank_transfer_payment = BankTransferPayment()
    order_processor_bank_transfer = OrderProcessor(bank_transfer_payment)
    order_processor_bank_transfer.process_order()
