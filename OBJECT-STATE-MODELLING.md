
# **Activity Diagrams for Critical Objects in the Online Appointment System**  

## **1. Appointment Booking Process**  
### **Explanation:**  
- The process begins when a **patient logs in** and selects an available time slot.  
- The system checks the doctor's availability.  
- If available, the **appointment is scheduled** and the **patient receives confirmation**.  
- If the doctor is unavailable, the patient must **choose a different slot**.  

```mermaid
graph TD;
    Start -->|Patient Logs In| CheckAvailability;
    CheckAvailability -->|Doctor Available| ScheduleAppointment;
    CheckAvailability -->|Doctor Not Available| ChooseDifferentSlot;
    ChooseDifferentSlot --> CheckAvailability;
    ScheduleAppointment --> SendConfirmation;
    SendConfirmation --> End;
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **2. Patient Registration & Login Flow**  
### **Explanation:**  
- A **new patient** registers in the system.  
- The system **validates the credentials**.  
- If valid, the **patient logs in** and can proceed to book an appointment.  
- If invalid, an **error message** is displayed.  

```mermaid
graph TD;
    Start -->|Patient Registers| ValidateCredentials;
    ValidateCredentials -->|Valid| Login;
    ValidateCredentials -->|Invalid| ShowError;
    ShowError -->|Retry| ValidateCredentials;
    Login --> ProceedToBooking;
    ProceedToBooking --> End;
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **3. Payment Processing Flow**  
### **Explanation:**  
- The patient initiates **payment for an appointment**.  
- The system processes the payment.  
- If **successful**, the appointment is confirmed.  
- If **failed**, the patient is prompted to try again or choose a different method.  
- Refunds can be requested if needed.  

```mermaid
graph TD;
    Start -->|Patient Initiates Payment| ProcessPayment;
    ProcessPayment -->|Success| ConfirmAppointment;
    ProcessPayment -->|Failure| ShowError;
    ShowError -->|Retry| ProcessPayment;
    ConfirmAppointment --> End;
    ConfirmAppointment -->|Refund Requested| ProcessRefund;
    ProcessRefund --> RefundComplete;
    RefundComplete --> End;

    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **4. Admin Reviewing Appointments**  
### **Explanation:**  
- Admins can **approve** or **reject** an appointment request.  
- If rejected, the patient is notified and asked to **reschedule**.  
- If approved, the system moves the appointment to **confirmed status**.  

```mermaid
graph TD;
    Start -->|Admin Reviews Appointment| Decision;
    Decision -->|Approved| ConfirmAppointment;
    Decision -->|Rejected| NotifyPatient;
    NotifyPatient -->|Reschedule| Start;
    ConfirmAppointment --> End;

    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **5. Notification Management Flow**  
### **Explanation:**  
- The system **generates notifications** when a patient books, cancels, or reschedules an appointment.  
- Notifications are **sent via email/SMS** and marked as read when viewed.  

```mermaid
graph TD;
    A[Start] -->|Event Occurs: Booking, Cancellation, Reschedule| B[Generate Notification];
    B -->|Send via Email or SMS| C[Send Notification];
    C -->|Patient Reads Notification| D[Mark as Read];
    D --> E[End];

    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style E fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **6. Doctor Availability Management**  
### **Explanation:**  
- A doctor is **available** by default.  
- If they start a session, they become **busy**.  
- If they **cancel or reschedule** an appointment, their availability changes accordingly.  

```mermaid
graph TD;
    Start -->|Doctor is Available| AcceptAppointment;
    AcceptAppointment -->|Doctor Starts Session| Busy;
    Busy -->|Doctor Finishes| Available;
    AcceptAppointment -->|Doctor Cancels| NotifyPatient;
    NotifyPatient -->|Reschedule| AcceptAppointment;
    Busy --> End;

    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```

---

## **7. Patient Feedback & Review Process**  
### **Explanation:**  
- After an appointment, patient can **submit feedback**.  
- The system **reviews** feedback before publishing it.  
- If rejected, the patient may be asked to **edit and resubmit**.  

```mermaid
graph TD;
    Start -->|Patient Submits Feedback| ReviewFeedback;
    ReviewFeedback -->|Approved| PublishFeedback;
    ReviewFeedback -->|Rejected| RequestEdit;
    RequestEdit -->|Patient Edits & Resubmits| ReviewFeedback;
    PublishFeedback --> End;

    style Start fill:#f9f,stroke:#333,stroke-width:2px;
    style End fill:#f9f,stroke:#333,stroke-width:2px;
```
