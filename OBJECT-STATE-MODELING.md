## **Object State Modeling with State Transition Diagrams**

### **1. Appointment State Transition**
```mermaid
stateDiagram
    [*] --> Scheduled
    Scheduled --> Confirmed : User confirms appointment
    Confirmed --> Completed : Appointment is attended
    Scheduled --> Canceled : User cancels appointment
    Confirmed --> Canceled : Canceled before completion
    Completed --> [*]
    Canceled --> [*]
```
**Explanation:**
- The **appointment** starts as **"Scheduled"** when a user books it.
- It moves to **"Confirmed"** when the user or system verifies it.
- If attended, it transitions to **"Completed"**; otherwise, it can be **"Canceled"** before completion.
- This addresses **FR-001: Users can schedule, confirm, and cancel appointments**.

---

### **2. User Account State Transition**
```mermaid
stateDiagram
    [*] --> Registered
    Registered --> LoggedIn : User enters valid credentials
    LoggedIn --> Booking : User books an appointment
    Booking --> LoggedOut : User logs out
    LoggedIn --> LoggedOut : Session timeout
    LoggedOut --> [*]
```
**Explanation:**
- The **user account** starts in the **"Registered"** state.
- After **logging in**, users can perform actions like booking an appointment.
- If the user logs out or the session expires, it returns to **"LoggedOut"**.
- This satisfies **FR-002: Users must register, log in, and log out**.

---

### **3. Payment State Transition**
```mermaid
stateDiagram
    [*] --> Pending
    Pending --> Processed : Payment is successful
    Processed --> Completed : Payment is verified
    Pending --> Failed : Payment declined
    Processed --> Refunded : User requests refund
    Completed --> [*]
    Failed --> [*]
    Refunded --> [*]
```
**Explanation:**
- Payments start in **"Pending"**.
- If successful, they move to **"Processed"**, and then **"Completed"**.
- If the transaction **fails**, it moves to **"Failed"**.
- Users can request a **refund** if eligible.
- This supports **FR-003: Secure payment processing and refunds**.

---

### **4. Admin Review State Transition**
```mermaid
stateDiagram
    [*] --> Reviewing
    Reviewing --> Approved : Meets criteria
    Reviewing --> Rejected : Fails criteria
    Approved --> [*]
    Rejected --> [*]
```
**Explanation:**
- The **admin reviews** appointment requests.
- If valid, the state transitions to **"Approved"**; if not, it is **"Rejected"**.
- This ensures **FR-004: Admins must approve or reject appointments**.

---

### **5. Notification State Transition**
```mermaid
stateDiagram
    [*] --> Generated
    Generated --> Sent : Notification dispatched
    Sent --> Read : User views notification
    Read --> [*]
```
**Explanation:**
- Notifications are **generated** automatically.
- Once **sent**, users can view them, transitioning to **"Read"**.
- This implements **FR-005: Users receive notifications for appointment updates**.

---

### **6. Doctor Availability State Transition**
```mermaid
stateDiagram
    [*] --> Available
    Available --> Busy : Doctor is attending an appointment
    Busy --> Available : Appointment ends
    Available --> Unavailable : Doctor is on leave
    Unavailable --> Available : Doctor returns
```
**Explanation:**
- Doctors start as **"Available"**.
- They become **"Busy"** when attending an appointment.
- If they take time off, their state transitions to **"Unavailable"**.
- This supports **FR-006: Track doctor availability for scheduling**.

---

### **7. System Session State Transition**
```mermaid
stateDiagram
    [*] --> Active
    Active --> Expired : Session timeout
    Active --> Terminated : User logs out
    Expired --> [*]
    Terminated --> [*]
```
**Explanation:**
- The session begins as **"Active"**.
- If the user remains idle, it **"Expires"**.
- If the user logs out, it transitions to **"Terminated"**.
- This ensures **FR-007: Automatic session expiration for security**.

---

### **8. Feedback State Transition**
```mermaid
stateDiagram
    [*] --> Submitted
    Submitted --> Reviewed : Admin verifies feedback
    Reviewed --> Published : Feedback is approved
    Reviewed --> Rejected : Feedback is removed
    Published --> [*]
    Rejected --> [*]
```
**Explanation:**
- Users **submit feedback**, which is **reviewed** by an admin.
- If approved, it is **"Published"**; otherwise, it is **"Rejected"**.
- This meets **FR-008: Users can submit feedback, which admins moderate**.
