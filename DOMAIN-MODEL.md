# Domain Model

| Entity      | Attributes                                                                 | Methods                            | Relationships                                                                 |
|-------------|----------------------------------------------------------------------------|------------------------------------|--------------------------------------------------------------------------------|
| **User**    | userID, name, email, phone, password, role                                 | login(), register(), updateProfile() | Can book many Appointments, makes Payments                                     |
| **Appointment** | appointmentID, dateTime, status, reason                                 | book(), cancel(), reschedule()     | Booked by one User, for one Service, with one Provider, has one Payment       |
| **Service** | serviceID, name, description, duration, price                               | listServices(), updateService()     | Linked to many Appointments, offered by many Providers                         |
| **Provider**| providerID, name, specialization, email, phone                              | viewSchedule(), updateAvailability() | Offers many Services, manages Schedules, has Appointments                      |
| **Schedule**| scheduleID, providerID, startTime, endTime, isAvailable (bool)             | checkAvailability(), updateSlot()   | Assigned to one Provider                                                       |
| **Payment** | paymentID, amount, method, status, timestamp                               | processPayment(), refund()          | Linked to one Appointment                                                      |
| **Notification** | notificationID, userID, message, timestamp, readStatus                | send(), markAsRead()                | Sent to Users for Appointment updates                                          |

---

## Relationships

- **User ↔ Appointment**: A User can book multiple Appointments.
- **Appointment ↔ Service**: Each Appointment is for one Service.
- **Appointment ↔ Provider**: An Appointment is with one Provider.
- **Provider ↔ Service**: A Provider can offer multiple Services.
- **Provider ↔ Schedule**: Each Provider has a Schedule to manage availability.
- **Appointment ↔ Payment**: Each Appointment is associated with a Payment.
- **User ↔ Notification**: Notifications are sent to Users regarding Appointments.

---

## Business Rules

1. A user **must be registered** to book an appointment.
2. A provider must have an **available schedule slot** to accept a booking.
3. Appointments can only be **rescheduled or cancelled** 24 hours before the appointment.
4. A user **cannot book overlapping appointments**.
5. Payments must be completed before an appointment is marked as **confirmed**.
6. A provider can only offer **services they are assigned to**.

---
