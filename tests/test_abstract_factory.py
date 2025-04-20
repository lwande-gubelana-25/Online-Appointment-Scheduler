import unittest
from creational_patterns.abstract_factory import EmailReminderFactory, SMSReminderFactory

class TestAbstractFactory(unittest.TestCase):

    def test_abstract_factory(self):
        print("Running Abstract Factory Test...")
        email_factory = EmailReminderFactory()
        sms_factory = SMSReminderFactory()
        
        email_reminder = email_factory.create_reminder()
        self.assertEqual(email_reminder.notify(), "Sending Email Reminder")
        print("Abstract Factory Test passed for Email reminder.")
        
        sms_reminder = sms_factory.create_reminder()
        self.assertEqual(sms_reminder.notify(), "Sending SMS Reminder")
        print("Abstract Factory Test passed for SMS reminder.")

if __name__ == "__main__":
    unittest.main()
