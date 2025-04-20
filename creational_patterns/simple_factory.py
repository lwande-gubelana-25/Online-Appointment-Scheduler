class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Sending notification: {self.message}"

class NotificationFactory:
    @staticmethod
    def create_notification(type_, message):
        if type_ == "email":
            return Notification(message)
        elif type_ == "sms":
            return Notification(f"SMS: {message}")
        elif type_ == "push":
            return Notification(f"Push: {message}")
        else:
            raise ValueError("Invalid notification type")

# Demo
if __name__ == "__main__":
    n = NotificationFactory.create_notification("email", "Appointment confirmed")
    print(n.send())
