# Define an abstract payment interface
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Implement specific payment methods

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of R{amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of R{amount}")

class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of R{amount}")

# High-level order processing module
class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_order(self, amount):
        # Some order processing logic
        print(f"Processing order of total amount R{amount}")

        # Delegating payment processing to the injected payment processor
        self.payment_processor.process_payment(amount)

# Client code
if __name__ == "__main__":
    # Example usage with Credit Card payment
    credit_card_payment = CreditCardPayment()
    order_processor_cc = OrderProcessor(credit_card_payment)
    order_processor_cc.process_order(10000)

    # Example usage with PayPal payment
    paypal_payment = PayPalPayment()
    order_processor_pp = OrderProcessor(paypal_payment)
    order_processor_pp.process_order(1500)
