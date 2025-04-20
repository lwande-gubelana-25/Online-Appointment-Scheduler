class Reminder:
    def notify(self):
        raise NotImplementedError()

class EmailReminder(Reminder):
    def notify(self):
        return "Sending Email Reminder"

class SMSReminder(Reminder):
    def notify(self):
        return "Sending SMS Reminder"

class ReminderFactory:
    def create_reminder(self):
        raise NotImplementedError()

class EmailReminderFactory(ReminderFactory):
    def create_reminder(self):
        return EmailReminder()

class SMSReminderFactory(ReminderFactory):
    def create_reminder(self):
        return SMSReminder()

# Demo
if __name__ == "__main__":
    factory = EmailReminderFactory()
    reminder = factory.create_reminder()
    print(reminder.notify())
