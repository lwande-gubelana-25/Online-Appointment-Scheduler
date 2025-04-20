import unittest
from creational_patterns.factory_method import PaymentFactory

class TestFactoryMethod(unittest.TestCase):

    def test_factory_method(self):
        print("Running Factory Method Test...")
        credit = PaymentFactory.get_processor("credit")
        self.assertEqual(credit.process(100), "Processing credit card payment of $100")
        print("Factory Method Test passed for Credit payment processor.")
        
        print("Testing with unsupported payment type...")
        with self.assertRaises(ValueError):
            PaymentFactory.get_processor("crypto")
        print("Factory Method Test passed for unsupported payment type.")

if __name__ == "__main__":
    unittest.main()
