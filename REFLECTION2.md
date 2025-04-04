## Reflection
### **Challenges in Choosing Granularity**
One of the main challenges was deciding **how detailed each state diagram should be**.  
- **Too much granularity** can make diagrams cluttered and hard to read. For instance, representing every minor user interaction (e.g., “Form Filled”, “Validation Passed”) adds noise.
- On the other hand, **too little detail** fails to capture critical system behavior, which is essential for both developers and testers.
- We struck a balance by focusing on **core state transitions** (e.g., “Scheduled”, “Confirmed”, “Cancelled”) that align directly with user and system actions defined in the functional requirements.

### **Aligning Diagrams with Agile User Stories**
Another challenge was **translating Agile user stories into meaningful object states**.
- User stories focus on **what the user wants to achieve**, while state diagrams show **how the system behaves** in response.
- For example, a user story like *“As a user, I want to cancel an appointment”* had to be reflected as transitions from “Scheduled” to “Cancelled” in the **Appointment** object.
- This required **careful mapping** between high-level user intentions and system state logic, ensuring traceability to both sprint tasks and functional requirements.

### **Comparison: State Diagrams vs Activity Diagrams**
| **Aspect**                 | **State Diagrams**                                         | **Activity Diagrams**                                  |
|---------------------------|------------------------------------------------------------|--------------------------------------------------------|
| **Focus**                  | Object behavior over time                                  | Sequence of activities and decisions                   |
| **Used For**               | Modeling system state transitions                         | Modeling workflows and business logic                  |
| **Strength**               | Great for lifecycle modeling of an object                  | Better at showing step-by-step processes               |
| **Example in Project**     | How an appointment moves from Scheduled → Confirmed → Done | How a user books an appointment step-by-step           |

In the project, **state diagrams** provided a **precise understanding of system behavior** per object (e.g., Appointment, UserAccount), while **activity diagrams** illustrated **user or admin workflows**. Each serves a different purpose in system modeling.
