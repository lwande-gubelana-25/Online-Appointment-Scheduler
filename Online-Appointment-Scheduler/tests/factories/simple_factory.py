class NotificationFactory:
    def create_notification(self, type_):
        if type_ == "email":
            return EmailNotification()
        elif type_ == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")

class EmailNotification:
    def send(self):
        return "Sending email notification"

class SMSNotification:
    def send(self):
        return "Sending SMS notification"
