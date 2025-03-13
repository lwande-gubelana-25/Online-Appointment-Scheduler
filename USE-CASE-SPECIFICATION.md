# Use Case Specifications
## Use Case 1: Book Appointment
- Actor: Patient
- Description: Allows patients to schedule an appointment with a doctor.
- Preconditions: Patient is registered and logged into the system.
- Postconditions: Appointment is successfully booked and recorded.
- Basic Flow:
  1. Patient logs into the system.
  2. Patient selects a doctor and preferred date/time.
  3. System checks the availability.
  4. Patient confirms the appointment.
  5. System sends confirmation notification.
- Alternative Flow:
If the selected slot is unavailable, the system suggests alternative times.

## Use Case 2: Cancel Appointment
- Actor: Patient
- Description: Allows patients to cancel a previously booked appointment.
- Preconditions: Patient has an existing appointment.
- Postconditions: Appointment is removed from the system.
- Basic Flow:
  1. Patient logs in and navigates to their scheduled appointments.
  2. Patient selects an appointment to cancel.
  3. System confirms cancellation.
  4. System notifies the doctor and patient.
- Alternative Flow:
If cancellation occurs within a restricted period (e.g., less than 24 hours before), a warning is displayed.

## Use Case 3: Modify Appointment
- Actor: Patient, Receptionist
- Description: Allows patients or receptionists to reschedule an appointment.
- Preconditions: Appointment exists in the system.
- Postconditions: Appointment details are updated.
- Basic Flow:
  1. User selects an existing appointment.
  2. User modifies the date, time, or doctor.
  3. System checks availability.
  4. System updates the appointment.
- Alternative Flow:
If no slots are available, the system suggests other options.

## Use Case 4: View Doctor Availability
- Actor: Patient
- Description: Allows patients to see available appointment slots.
- Preconditions: Patient is logged in.
- Postconditions: Availability is displayed.
- Basic Flow:
  1. Patient selects a doctor.
  2. System displays available time slots.
- Alternative Flow:
If no slots are available, the system provides an option to request a notification when a slot opens.

## Use Case 5: Send Appointment Reminders
- Actor: System
- Description: Automatically sends appointment reminders to patients.
- Preconditions: An appointment is scheduled.
- Postconditions: Notification is sent to the patient.
- Basic Flow:
  1. System checks upcoming appointments.
  2. System sends a reminder via email or SMS.
- Alternative Flow:
If a message fails to send, the system retries after some time.

## Use Case 6: Process Payment
- Actor: Patient
- Description: Allows patients to pay for their appointment.
- Preconditions: An appointment is booked.
- Postconditions: Payment is confirmed and recorded.
- Basic Flow:
  1. Patient selects a payment method.
  2. System processes the payment.
  3. System confirms and generates a receipt.
- Alternative Flow:
If payment fails, the system displays an error message and allows retry.

## Use Case 7: Verify Insurance
- Actor: System, Insurance Provider
- Description: Ensures a patient’s insurance coverage is valid.
- Preconditions: Patient has entered insurance details.
- Postconditions: Insurance is verified, or an error is flagged.
- Basic Flow:
  1. System sends insurance details to the provider.
  2. Insurance provider confirms or denies coverage.
- Alternative Flow:
If verification fails, the system requests an alternative payment method.

## Use Case 8: Generate Reports
- Actor: Admin
- Description: Generates statistical and analytical reports on appointments.
- Preconditions: Admin is logged in.
- Postconditions: Reports are generated and available for viewing.
- Basic Flow:
  1. Admin selects report type.
  2. System compiles data.
  3. System generates the report.
- Alternative Flow:
If no data is available, an error message is displayed.
