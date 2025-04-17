# Online Appointment Scheduling System

## Description:
This is a system for managing patient appointments with healthcare providers.

## Links to Documents:
### Assignment 3
- [System Specification](SPECIFICATION.md)
- [Architecture](ARCHITECTURE.md)

### Assignment 4
- [Functional Requirements](FUNTIONAL.md)
-  [Non-Functional Requirements](NON-FUNCTIONAL-REQUIREMENTS.md)
-  [Stakeholder Analysis](STAKEHOLDER.md)
-  [Documentation](DOCUMENTATION.md)

### Assignment 5
- [Use Case Diagram](USE-CASE-DIAGRAM.md)
- [Use Case Specification](USE-CASE-SPECIFICATION.md)
- [Test Case Development](TEST-CASE.md)
- [Dcumentation](DOCUMENTATION2.md)

  ### Assignment 6
- [User Story Creation](USER-STORY-CREATION.md)
- [Product Backlog Creation](PRODUCT-BACKLOG.md)
- [Sprint Planning](SPRINT-PLAN.md)
- [Documentation](DOCUMENTATION3.md)

  ### Assignment 7
  - [Template Analysis and Selection](TEMPLATE-ANALYSIS-AND-SELECTION.md)
  - [Kanban Board Explanation](KANBAN-BOARD-EXPLANATION.md)
  - [Reflection](REFLECTION.md)
 
  - ![Project Screenshot](https://github.com/lwande-gubelana-25/Online-Appointment-Scheduler/blob/main/Screenshot%20(105).png?raw=true)
  - ![Project Screenshot](https://github.com/lwande-gubelana-25/Online-Appointment-Scheduler/blob/main/Screenshot%20(106).png?raw=true)

### Assignment 8
### Project Documentation

### **State Transition Diagrams**
This project uses **UML State Transition Diagrams** to model system behavior.

## **Diagrams & Explanations**
- [Object State Modeling](OBJECT-STATE-MODELING.md)
- [Activity Workflow Modeling](ACTIVITY-WORKFLOW-MODELING.md)

Each diagram is **mapped to functional requirements** and **user stories from previous assignments** for traceability.

## **Sprint Integration**
These diagrams align with **Assignment 6’s sprint plan**, ensuring that:
- All **user stories** have state-based representations.
- Functional flows match Agile development practices.

For full details, check the **[Sprint Planning Document](SPRINT-PLAN.md)**.

- [Intergration](INTERGRATION.md)
- [Reflection](REFLECTION2.md)

  ### Assignment 9
  - [Domain Model](DOMAIN-MODEL.md)
  - [Class Diagram in Mermaid.js](CLASS-DIAGRAM.md)
  - [Reflection](REFLECTION3.md)
 
 ### Assignment 10
 
#### Language Choice & Key Design Decisions

#### Language Choice: Python
I chose **Python** for this project due to its simplicity, readability, and quick development cycle. Python is particularly well-suited for object-oriented design, making it ideal for implementing real-world concepts like appointments, notifications, payments, and scheduling.

Other reasons for choosing Python include:
- Wide support for built-in libraries (e.g., `datetime`).
- Easy-to-read syntax, which enhances collaboration and maintainability.

#### Key Design Decisions

- **Object-Oriented Design (OOP):**  
  Classes were used to model real-world entities like `Appointment`, `Payment`, `Notification`, `Schedule`, and their associated behavior through methods like `book()`, `cancel()`, `processPayment()`, and `markAsRead()`.

- **Modularity:**  
  Each class is self-contained, representing a single responsibility. This makes the codebase easy to maintain, test, and extend in the future.

- **State Tracking:**  
  Attributes like `status` (for appointments and payments) and `read` (for notifications) were used to track state and enable condition-based logic (e.g., only refund if payment was completed).

- **Simple Simulations:**  
  Instead of integrating real APIs or databases at this stage, behaviors like `send()`, `processPayment()`, and `refund()` simulate realistic actions using console output, allowing for focus on structure and logic before full implementation.

- **Extensibility:**  
  This structure lays a solid foundation for adding features like persistence (databases), user input interfaces, or web integration in future phases.

---
