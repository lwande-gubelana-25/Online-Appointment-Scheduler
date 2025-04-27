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

  ## Link to src directory
  -[src directory](project-root)
  the src directory is in the project-root directory.

---

# Creational Patterns  Implementation

This project implements all six **creational design patterns** in Python, tailored for an **online appointment scheduling system**. Each pattern is used in a specific context that fits real-world use cases.

---

## Simple Factory Pattern
**Use Case:** Creating notifications (email, SMS, push).

**Why?** Centralizing notification creation avoids tightly coupling clients to specific notification types.

**Implementation:** `NotificationFactory.create_notification(type, message)`

---

## Factory Method Pattern
**Use Case:** Delegating payment processing.

**Why?** Different payment methods (Credit Card, PayPal) have their own logic. The factory method delegates instantiation to the correct processor.

**Implementation:** `PaymentFactory.get_processor(method)` returns a subclass of `PaymentProcessor`

---

##  Abstract Factory Pattern
**Use Case:** Generating reminder types as a family (email, SMS).

**Why?** Abstract Factory allows for generating a suite of related objects (reminders) without specifying their exact classes.

**Implementation:** `EmailReminderFactory` and `SMSReminderFactory` both implement `ReminderFactory`

---

##  Builder Pattern
**Use Case:** Constructing appointment objects step-by-step.

**Why?** Appointments often require optional fields (e.g., note, time). Builder enables flexible and readable object creation.

**Implementation:** `AppointmentBuilder().set_provider(...).set_service(...).build()`

---

##  Prototype Pattern
**Use Case:** Cloning predefined service types.

**Why?** Instead of creating service objects from scratch every time, clone templates to save setup time.

**Implementation:** `ServicePrototype.clone()` uses deep copy

---

##  Singleton Pattern
**Use Case:** Managing appointment instances globally.

**Why?** We need only one instance of `AppointmentManager` to track system-wide appointments, preventing duplication or sync issues.

**Implementation:** `AppointmentManager` overrides `__new__` to return the same instance

---

## Summary Table
| Pattern          | Used For                    | Key Class / File                          |
|------------------|-----------------------------|--------------------------------------------|
| Simple Factory   | Notifications               | `simple_factory.py`                        |
| Factory Method   | Payment processors          | `factory_method.py`                        |
| Abstract Factory | Reminder families           | `abstract_factory.py`                      |
| Builder          | Step-by-step appointments   | `builder.py`                               |
| Prototype        | Cloning service templates   | `prototype.py`                             |
| Singleton        | Shared appointment manager  | `singleton.py`                             |

## Link to creational patterns
-[Creational Pattern](creational_patterns)

## Link to Use testing
- [Use Testiing](tests)
- [Changelog](CHANGELOG.md)

# Assignment 11
  
## Repository Interface Design

I implemented a generic `Repository<T, ID>` interface using Python's `abc` (Abstract Base Classes) and `generics`.
This design was chosen because:

- **Generic Reuse**: Allows reuse of the standard CRUD operations across all entities like `User`, `Appointment`, `Service`, and `Provider`.
- **Flexibility**: Each entity-specific repository can extend the base `Repository` without rewriting basic methods.
- **Maintainability**: If the CRUD logic ever changes globally, we only need to update it once.
- **Compliance**: Follows standard Repository pattern practices seen in Java/Spring and other enterprise applications.

Example:

- `UserRepository` extends `Repository<User, String>`
- `AppointmentRepository` extends `Repository<Appointment, String>`

This ensures clean, modular, and scalable code.

## In-Memory Implementation

An in-memory implementation of repositories was created using simple Python dictionaries (HashMap equivalent).

Benefits:
- **Fast and lightweight**: No external dependencies needed.
- **Ideal for Unit Testing**: Allows verifying business logic without setting up a database.
- **Easy to extend**: Later we can replace InMemoryRepository with DatabaseRepository following the same interface.

Example:

- `InMemoryUserRepository` implements `save()`, `find_by_id()`, `find_all()`, and `delete()` with `_storage` dict.

This approach supports Agile development by enabling early testing before full persistence is implemented.

## Storage Abstraction Mechanism

I implemented a `RepositoryFactory` class to abstract the repository creation.

Why Factory Pattern?

- **Centralized control**: All repository creation is managed through one place.
- **Storage flexibility**: Easily switch from `InMemoryUserRepository` to `DatabaseUserRepository` in future without changing service code.
- **Future extensibility**: Support for different storage types like NoSQL, Cloud Storage, etc.


- [Repositories](repositories)
- [Factories](factories)
- [Updated Class Diagram](CLASS-DIAGRAM.md)
