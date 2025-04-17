import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime

from src.user import User
from src.service import Service
from src.provider import Provider
from src.schedule import Schedule
from src.payment import Payment
from src.appointment import Appointment
from src.notification import Notification


# class user
class User:
    def __init__(self, user_id, name, email, phone, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.role = role

    def login(self, email_input, password_input):
        if self.email == email_input and self.password == password_input:
            return f"Welcome {self.name}, login successful!"
        else:
            return "Invalid credentials."


user = User("U001", "Lwande", "lwandegu@gmail.com", "0621643399", "password123", "patient")

print(user.login("lwandegu@gmail.com", "password123"))

# Create service
class Service:
    def __init__(self, service_id, name, description, duration, price):
        self.service_id = service_id
        self.name = name
        self.description = description
        self.duration = duration  # in minutes
        self.price = price

service = Service("S001", "Dental Checkup", "Basic dental check", 30, 120.0)
print(service.name)  

# Create provider
class Provider:
    def __init__(self, provider_id, name, specialty, email, phone):
        self.provider_id = provider_id
        self.name = name
        self.specialty = specialty
        self.email = email
        self.phone = phone

# class Provider:
provider = Provider("P001", "Dr. Mngambi", "Dentist", "mngambi@clinic.com", "0823456789")
print(provider.name) 

# Create schedule
from datetime import datetime

class Schedule:
    from datetime import datetime

class Schedule:
    def __init__(self, schedule_id, start_time, end_time):
        self.schedule_id = schedule_id
        self.start_time = start_time
        self.end_time = end_time

    def display(self):
        print(f"Schedule ID: {self.schedule_id}")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")

    def checkAvailability(self, start_time, end_time):
        """
        Check if the provided time slot is available.
        Returns True if available, False if there is an overlap.
        """
        if start_time >= self.end_time or end_time <= self.start_time:
            return True  # No overlap, the slot is available
        else:
            return False  # There is an overlap, the slot is not available

    def updateSlot(self, new_start_time, new_end_time):
        """
        Update the schedule with new start and end times.
        """
        self.start_time = new_start_time
        self.end_time = new_end_time
        print("Schedule updated successfully.")

# Create an instance of the Schedule class
schedule = Schedule("SCH001", datetime(2025, 5, 1, 10, 0), datetime(2025, 5, 1, 10, 30))

# Display the current schedule
schedule.display()

# Check if a new time slot is available
new_start = datetime(2025, 5, 1, 11, 0)
new_end = datetime(2025, 5, 1, 11, 30)
is_available = schedule.checkAvailability(new_start, new_end)

if is_available:
    print("The time slot is available.")
else:
    print("The time slot is not available.")


# Create payment
from datetime import datetime

class Payment:
    def __init__(self, payment_id, amount, method, status, date):
        self.payment_id = payment_id
        self.amount = amount
        self.method = method
        self.status = status
        self.date = date

    def display(self):
        print(f"Payment ID: {self.payment_id}")
        print(f"Amount: R{self.amount}")
        print(f"Method: {self.method}")
        print(f"Status: {self.status}")
        print(f"Date: {self.date}")

    def processPayment(self):
        """
        Simulate processing the payment.
        If the payment status is 'Pending', it will be marked as 'Completed'.
        """
        if self.status == "Pending":
            self.status = "Completed"
            print(f"Payment {self.payment_id} processed successfully.")
        else:
            print(f"Payment {self.payment_id} has already been processed or refunded.")

    def refund(self):
        """
        Simulate processing a refund.
        If the payment status is 'Completed', it will be marked as 'Refunded'.
        """
        if self.status == "Completed":
            self.status = "Refunded"
            print(f"Payment {self.payment_id} refunded successfully.")
        else:
            print(f"Payment {self.payment_id} cannot be refunded because it is not completed.")

# Create an instance of the Payment class
payment = Payment("PAY001", 140.0, "Card", "Pending", datetime.now())

# Display the current payment details
payment.display()

# Process the payment
payment.processPayment()

# Display the updated payment details
payment.display()

# Try to refund the payment
payment.refund()

# Display the final payment details
payment.display()



from datetime import datetime

# Dummy Service class
class Service:
    def __init__(self, service_id, name):
        self.service_id = service_id
        self.name = name

# Dummy Provider class
class Provider:
    def __init__(self, provider_id, name):
        self.provider_id = provider_id
        self.name = name

# Payment class from earlier
class Payment:
    def __init__(self, payment_id, amount, method, status, date):
        self.payment_id = payment_id
        self.amount = amount
        self.method = method
        self.status = status
        self.date = date

    def display(self):
        print(f"Payment ID: {self.payment_id}")
        print(f"Amount: R{self.amount}")
        print(f"Method: {self.method}")
        print(f"Status: {self.status}")
        print(f"Date: {self.date}")

    def processPayment(self):
        if self.status == "Pending":
            self.status = "Completed"
            print(f"Payment {self.payment_id} processed successfully.")
        else:
            print(f"Payment {self.payment_id} has already been processed or refunded.")

    def refund(self):
        if self.status == "Completed":
            self.status = "Refunded"
            print(f"Payment {self.payment_id} refunded successfully.")
        else:
            print(f"Payment {self.payment_id} cannot be refunded because it is not completed.")

# Appointment class
class Appointment:
    def __init__(self, appointment_id, date_time, status, reason, service, provider, payment):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.status = status
        self.reason = reason
        self.service = service
        self.provider = provider
        self.payment = payment

    def display(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Date & Time: {self.date_time}")
        print(f"Status: {self.status}")
        print(f"Reason: {self.reason}")
        print(f"Service: {self.service.name}")
        print(f"Provider: {self.provider.name}")
        print(f"Payment Status: {self.payment.status}")

    def book(self):
        if self.status == "Pending":
            self.status = "Booked"
            self.payment.processPayment()
            print(f"Appointment {self.appointment_id} has been booked.")
        else:
            print(f"Appointment {self.appointment_id} is already {self.status}.")

    def cancel(self):
        if self.status in ["Pending", "Booked"]:
            self.status = "Cancelled"
            self.payment.refund()
            print(f"Appointment {self.appointment_id} has been cancelled.")
        else:
            print(f"Appointment {self.appointment_id} cannot be cancelled because it is {self.status}.")

    def reschedule(self, new_date_time):
        if self.status == "Booked":
            print(f"Appointment {self.appointment_id} rescheduled from {self.date_time} to {new_date_time}.")
            self.date_time = new_date_time
        else:
            print(f"Only booked appointments can be rescheduled.")

# Create related instances
service = Service("SVC001", "Dental Checkup")
provider = Provider("PRV001", "Dr. Mngambi")
payment = Payment("PAY001", 140.0, "Card", "Pending", datetime.now())

# Create and use appointment
appointment = Appointment("APT001", datetime(2025, 5, 1, 10, 0), "Pending", "Toothache", service, provider, payment)

# Display appointment
appointment.display()

# Book appointment
appointment.book()
appointment.display()

# Reschedule appointment
appointment.reschedule(datetime(2025, 5, 2, 11, 0))
appointment.display()

# Cancel appointment
appointment.cancel()
appointment.display()


# from datetime import datetime

class Notification:
    def __init__(self, notification_id, message, timestamp):
        self.notification_id = notification_id
        self.message = message
        self.timestamp = timestamp
        self.read = False  # Track read status

    def display(self):
        status = "Read" if self.read else "Unread"
        print(f"[{self.timestamp}] Notification ({self.notification_id}) - {status}: {self.message}")

    def send(self):
        print(f"Sending notification: {self.message}")

    def markAsRead(self):
        if not self.read:
            self.read = True
            print(f"Notification {self.notification_id} marked as read.")
        else:
            print(f"Notification {self.notification_id} is already marked as read.")

# Example usage
notification = Notification("N001", "Your appointment has been confirmed.", datetime.now())

# Display the notification
notification.display()

# Send the notification
notification.send()

# Mark as read
notification.markAsRead()

# Display again to see the updated status
notification.display()
