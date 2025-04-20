import unittest
from creational_patterns.builder import AppointmentBuilder

class TestBuilder(unittest.TestCase):

    def test_builder(self):
        print("Running Builder Test...")
        builder = AppointmentBuilder()
        appointment = builder.set_provider("Dr. Max").set_service("Cleaning").build()
        self.assertEqual(appointment.provider, "Dr. Max")
        self.assertEqual(appointment.service, "Cleaning")
        print("Builder Test passed for appointment creation.")

    def test_builder_edge_case(self):
        print("Running Builder Edge Case Test...")
        builder = AppointmentBuilder()
        appointment = builder.build()  # No fields set
        self.assertIsNone(appointment.date_time)
        self.assertIsNone(appointment.provider)
        print("Builder Edge Case Test passed for empty appointment.")

        print("Testing with invalid provider input...")
        with self.assertRaises(ValueError):
            builder.set_provider("")  # Empty provider should raise an error
        print("Builder Edge Case Test passed for invalid provider.")

if __name__ == "__main__":
    unittest.main()
