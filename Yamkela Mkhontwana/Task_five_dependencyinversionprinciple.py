from abc import ABC, abstractmethod

# Part 1: Define high-level order processing module

class Order:
    def __init__(self, order_id, total_amount):
        self.order_id = order_id
        self.total_amount = total_amount

# Part 2: Define high-level order processing module (updated)

class OrderProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_order(self, order):
        # Process order logic
        print(f"Processing order {order.order_id}")

        # Delegate payment to the payment gateway
        self.payment_gateway.process_payment(order.total_amount)

# Part 3: Define abstraction for payment modules

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Part 4: Implement low-level payment modules

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class BankTransferPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of {amount}")

# Part 5: Usage example (updated)

# Create instances of orders
order1 = Order("Order123", 100.0)
order2 = Order("Order456", 150.0)

# Create an instance of OrderProcessor with the initial payment method
order_processor = OrderProcessor(CreditCardPayment())

# Process orders with the initial payment method
order_processor.process_order(order1)

# Switching payment method without modifying the OrderProcessor
order_processor.payment_gateway = PayPalPayment()
order_processor.process_order(order2)
