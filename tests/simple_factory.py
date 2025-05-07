from tests.factories.simple_factory
import NotificationFactory

class NotificationFactory:
    def create_notification(self, type):
        if type == "email":
            return EmailNotification()
        elif type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification type: {type}")
