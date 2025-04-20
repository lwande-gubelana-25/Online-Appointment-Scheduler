# /tests/test_patterns.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from creational_patterns.simple_factory import NotificationFactory
from creational_patterns.factory_method import PaymentFactory
from creational_patterns.abstract_factory import EmailReminderFactory, SMSReminderFactory
from creational_patterns.builder import AppointmentBuilder
from creational_patterns.prototype import ServicePrototype
from creational_patterns.singleton import AppointmentManager

class TestCreationalPatterns(unittest.TestCase):

    def test_simple_factory(self):
        email = NotificationFactory.create_notification("email", "Test Email")
        self.assertEqual(email.send(), "Sending notification: Test Email")
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("unknown", "Invalid")

    def test_factory_method(self):
        credit = PaymentFactory.get_processor("credit")
        self.assertEqual(credit.process(100), "Processing credit card payment of $100")
        with self.assertRaises(ValueError):
            PaymentFactory.get_processor("crypto")

    def test_abstract_factory(self):
        email_factory = EmailReminderFactory()
        sms_factory = SMSReminderFactory()
        self.assertEqual(email_factory.create_reminder().notify(), "Sending Email Reminder")
        self.assertEqual(sms_factory.create_reminder().notify(), "Sending SMS Reminder")

    def test_builder(self):
        builder = AppointmentBuilder()
        appointment = builder.set_provider("Dr. Max").set_service("Cleaning").build()
        self.assertEqual(appointment.provider, "Dr. Max")
        self.assertEqual(appointment.service, "Cleaning")

    def test_builder_edge_case(self):
        builder = AppointmentBuilder()
        appointment = builder.build()  # No fields set
        self.assertIsNone(appointment.date_time)
        self.assertIsNone(appointment.provider)

    def test_prototype(self):
        service = ServicePrototype("S001", "Consultation", "General advice", 30, 200)
        cloned = service.clone()
        self.assertEqual(cloned.name, service.name)
        self.assertIsNot(cloned, service)  # Ensure it's a clone

    def test_singleton(self):
        mgr1 = AppointmentManager()
        mgr2 = AppointmentManager()
        mgr1.add_appointment("Checkup")
        self.assertIn("Checkup", mgr2.list_appointments())
        self.assertIs(mgr1, mgr2)  # Same instance

if __name__ == "__main__":
    unittest.main()
