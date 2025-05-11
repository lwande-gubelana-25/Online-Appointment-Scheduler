from tests.simple_factory import NotificationFactory

def test_email_notification():
    factory = NotificationFactory()
    notification = factory.create_notification("email")
    assert notification.send() == "Sending email notification"

def test_sms_notification():
    factory = NotificationFactory()
    notification = factory.create_notification("sms")
    assert notification.send() == "Sending SMS notification"
