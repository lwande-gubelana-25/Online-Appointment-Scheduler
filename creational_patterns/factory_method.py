class PaymentProcessor:
    def process(self, amount):
        raise NotImplementedError()

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing PayPal payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Unsupported payment method")

# Demo
if __name__ == "__main__":
    processor = PaymentFactory.get_processor("credit")
    print(processor.process(200))
