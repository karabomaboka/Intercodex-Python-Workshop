# Exercise 5: Dependency Inversion Principle (DIP)
# Scenario: Imagine creating an e-commerce application that processes orders and payments. The payment process can be done through various methods (e.g., credit card, PayPal, bank transfer).
# Task: Develop the system in a way that the high-level order processing module is not dependent on the low-level payment modules. Think about how you would design the system to easily accommodate new payment methods in the future.

class OrderProcessingModule:
    def process_order(self, order):
        # Get the payment method from the order.
        payment_method = order.get_payment_method()

        # Create a payment gateway object for the payment method.
        payment_gateway = PaymentGatewayFactory.create_payment_gateway(payment_method)

        # Process the payment through the payment gateway.
        payment_gateway.process_payment(order)


class PaymentGatewayFactory:
    def create_payment_gateway(self, payment_method):
        if payment_method == "credit_card":
            return CreditCardPaymentGateway()
        elif payment_method == "paypal":
            return PayPalPaymentGateway()
        elif payment_method == "bank_transfer":
            return BankTransferPaymentGateway()
        else:
            raise ValueError("Unsupported payment method: {}".format(payment_method))


class CreditCardPaymentGateway:
    def process_payment(self, order):
        # Process the payment through the credit card payment gateway.


     class PayPalPaymentGateway:
      def process_payment(self, order):
        # Process the payment through the PayPal payment gateway.


       class BankTransferPaymentGateway:
        def process_payment(self, order):
        