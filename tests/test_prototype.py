import unittest
from creational_patterns.prototype import ServicePrototype

class TestPrototype(unittest.TestCase):

    def test_prototype(self):
        print("Running Prototype Test...")
        service = ServicePrototype("S001", "Consultation", "General advice", 30, 200)
        cloned = service.clone()
        self.assertEqual(cloned.name, service.name)
        self.assertIsNot(cloned, service)  # Ensure it's a clone
        print("Prototype Test passed for basic clone.")

        print("Testing with complex prototype (nested objects)...")
        service_with_details = ServicePrototype("S002", "Therapy", "Physical Therapy", 60, 500)
        service_with_details.details = {"location": "Room 101", "time": "10 AM"}
        cloned_details = service_with_details.clone()
        self.assertEqual(cloned_details.details, service_with_details.details)
        print("Prototype Test passed for complex clone with details.")

if __name__ == "__main__":
    unittest.main()
