from tests.factories.simple_factory import NotificationFactory

class TestSimpleFactory(unittest.TestCase):

    def test_simple_factory(self):
        print("Running Simple Factory Test...")
        email = NotificationFactory.create_notification("email", "Test Email")
        self.assertEqual(email.send(), "Sending notification: Test Email")
        print("Simple Factory Test passed for Email notification.")
        
        print("Testing with invalid notification type...")
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("unknown", "Invalid")
        print("Simple Factory Test passed for invalid type.")

if __name__ == "__main__":
    unittest.main()
