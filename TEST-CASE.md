# Test Case Development

| Test Case ID | Requirement ID | Description                        | Steps                                                                | Expected Result                  | 
| ------------ | -------------- | ---------------------------------- | -------------------------------------------------------------------- | -------------------------------- | 
| TC-001       | FR-001         | Patient books an appointment       | 1. Login 2. Select doctor 3. Confirm slot                            | Appointment booked successfully  |                       
| TC-002       | FR-002         | Patient cancels an **appointment** | 1. Login 2. Select booked slot 3. Cancel                             | Appointment removed successfully |                       
| TC-003       | FR-003         | System sends appointment reminders | 1. System triggers reminder 2. Email/SMS sent                        | Reminder received by patient     |                       
| TC-004       | FR-004         | Patient modifies an appointment    | 1. Login 2. Select booked appointment 3. Update details 4. Confirm   | Appointment updated successfully |                       
| TC-005       | FR-005         | Patient views doctor availability  | 1. Login 2. Select doctor 3. View available slots                    | Available slots displayed        |                       
| TC-006       | FR-006         | System verifies insurance coverage | 1. Patient enters insurance details 2. System verifies with provider | Insurance status updated         |                       
| TC-007       | FR-007         | Patient makes a payment            | 1. Login 2. Select appointment 3. Choose payment method 4. Confirm   | Payment processed successfully   |                       
| TC-008       | FR-008         | Admin generates reports            | 1. Login as admin 2. Select report type 3. Generate report           | Report displayed successfully    |               

# Non-functional Tests

| Test Case ID | Requirement ID | Description      | Test Scenario                                        | Expected Result            | 
| ------------ | -------------- | ---------------- | ---------------------------------------------------- | -------------------------- | 
| NTC-001      | NFR-001        | Performance Test | Simulate 1,000 concurrent users booking appointments | Response time ≤ 3 seconds  |                     
| NTC-002      | NFR-002        | Security Test    | Attempt unauthorized access to patient data          | Unauthorized access denied |                     


