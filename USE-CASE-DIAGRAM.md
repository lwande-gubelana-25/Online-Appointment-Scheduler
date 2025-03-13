# Actors and Use Cases
## Actors:
1. Patient – Requests, books, and cancels appointments.
2. Doctor – Manages availability and consultations.
3. Receptionist – Handles manual appointment scheduling.
4. Admin – Manages user roles and permissions.
5. System – Automates notifications and reminders.
6. nsurance Provider – Verifies coverage for patients.

## Use Cases:
1. Book Appointment – Patient schedules an appointment.
2. Cancel Appointment – Patient cancels a scheduled appointment.
3. Modify Appointment – Patient or receptionist updates appointment details.
4. View Doctor Availability – Patients check available slots.
5. Send Appointment Reminders – System notifies users.
6. Process Payment – Patient completes payment for consultation.
7. Verify Insurance – System confirms coverage.
8. Generate Reports – Admin generates analytics reports.

# Explanation:
- The Patient can initiate "Book Appointment," "Cancel Appointment," and "Modify Appointment" use cases.
- The Doctor manages availability and interacts with booked appointments.
- The Receptionist provides manual scheduling support.
- The Admin ensures smooth system operation and generates reports.
- The System automates reminders and insurance verification.
- The Insurance Provider interacts with the system to confirm coverage.

# How the Diagram Addresses Stakeholder Concerns
- Patients can book, cancel, and modify their appointments, ensuring a flexible and user-friendly system.
- Doctors can manage their schedules, addressing concerns about workload management.
- Receptionists can assist in appointment handling, reducing errors and improving efficiency.
- The system automates appointment reminders, reducing missed appointments.
- Insurance providers can verify coverage directly, improving the billing process.
- Administrators have access to reports, ensuring compliance and operational monitoring.

```mermaid
graph TD;
    Patient -->|Books| BookAppointment;
    Patient -->|Cancels| CancelAppointment;
    Patient -->|Modifies| ModifyAppointment;
    Patient -->|Views| ViewDoctorAvailability;
    System -->|Sends| SendAppointmentReminders;
    Patient -->|Pays| ProcessPayment;
    System -->|Verifies| VerifyInsurance;
    Admin -->|Generates| GenerateReports;
    Doctor -->|Manages| ManageAppointments;
    Receptionist -->|Schedules| BookAppointment;
    Receptionist -->|Updates| ModifyAppointment;
    InsuranceProvider -->|Verifies| VerifyInsurance;
