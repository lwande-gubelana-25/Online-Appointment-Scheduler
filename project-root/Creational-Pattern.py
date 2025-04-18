# /creational_patterns/simple_factory.py
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Sending notification: {self.message}"

class EmailNotification(Notification):
    pass

class SMSNotification(Notification):
    pass

class PushNotification(Notification):
    pass

class NotificationFactory:
    @staticmethod
    def create_notification(type_, message):
        if type_ == "email":
            return EmailNotification(message)
        elif type_ == "sms":
            return SMSNotification(message)
        elif type_ == "push":
            return PushNotification(message)
        else:
            raise ValueError("Unknown notification type")

print(NotificationFactory.create_notification("email", "Check-up Reminder").send())
print(NotificationFactory.create_notification("sms", "Upcoming Appointment").send())


# /creational_patterns/factory_method.py
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing PayPal payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Unsupported payment method")

print(PaymentFactory.get_processor("credit").process(150.0))
print(PaymentFactory.get_processor("paypal").process(80.0))


# /creational_patterns/abstract_factory.py
from abc import ABC, abstractmethod

class Reminder:
    def notify(self):
        pass

class EmailReminder(Reminder):
    def notify(self):
        return "Sending Email Reminder"

class SMSReminder(Reminder):
    def notify(self):
        return "Sending SMS Reminder"

class ReminderFactory(ABC):
    @abstractmethod
    def create_reminder(self):
        pass

class EmailReminderFactory(ReminderFactory):
    def create_reminder(self):
        return EmailReminder()

class SMSReminderFactory(ReminderFactory):
    def create_reminder(self):
        return SMSReminder()

print(EmailReminderFactory().create_reminder().notify())
print(SMSReminderFactory().create_reminder().notify())


# /creational_patterns/builder.py
class Appointment:
    def __init__(self, date_time=None, provider=None, service=None, note=""):
        self.date_time = date_time
        self.provider = provider
        self.service = service
        self.note = note

    def confirm(self):
        return f"Appointment confirmed with {self.provider} for {self.service}"

class AppointmentBuilder:
    def __init__(self):
        self.appointment = Appointment()

    def set_date_time(self, date_time):
        self.appointment.date_time = date_time
        return self

    def set_provider(self, provider):
        self.appointment.provider = provider
        return self

    def set_service(self, service):
        self.appointment.service = service
        return self

    def add_note(self, note):
        self.appointment.note = note
        return self

    def build(self):
        return self.appointment

print(AppointmentBuilder().set_provider("Dr. Mngambi").set_service("Teeth Cleaning").build().confirm())


# /creational_patterns/prototype.py
import copy

class ServicePrototype:
    def __init__(self, service_id, name, description, duration, price):
        self.service_id = service_id
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

base_service = ServicePrototype("S001", "Dental Check", "Basic inspection", 30, 100.0)
cloned_service = base_service.clone()
print(f"Cloned service: {cloned_service.name}, ${cloned_service.price}")


# /creational_patterns/singleton.py
class AppointmentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._appointments = []
        return cls._instance

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    def list_appointments(self):
        return self._appointments

manager1 = AppointmentManager()
manager2 = AppointmentManager()
manager1.add_appointment("Appointment with Dr. Lee")
print(manager2.list_appointments())  # Should include the above
print("Same instance:", manager1 is manager2)
