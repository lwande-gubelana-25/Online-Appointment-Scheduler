# Reflection
Designing the domain model and class diagram for the **Online Appointment Scheduling System** presented a number of challenges and valuable learning experiences. While I have worked on system design before, this task required a deeper and more structured application of object-oriented principles, particularly abstraction, relationships, and ensuring alignment with prior project artifacts like use cases and state diagrams.

## 1. Challenges in Designing the Domain Model and Class Diagram

One of the main challenges I encountered was in determining the appropriate **level of abstraction** for each class. Initially, it was tempting to create too many specialized classes for different actors and services, which would have complicated the model. I had to carefully balance **granularity**—choosing which entities should be represented as their own classes and which details could be encapsulated as attributes or methods.

Defining **relationships between classes** also proved tricky. For example, deciding whether a `User` should be directly connected to a `Service` or whether the `Appointment` should act as an intermediary required a lot of thought. Eventually, I recognized that the `Appointment` entity was the logical connector between users, services, and providers, acting as the core transaction in the system.
Another difficulty was defining **meaningful methods** for each class. It was easy to list basic attributes, but I needed to think more deeply about the behaviors and responsibilities of each object. This required revisiting user stories and functional requirements to ensure that the methods aligned with actual use cases (e.g., booking, cancelling, rescheduling, and processing payments).

## 2. Alignment with Previous Assignments

The class diagram aligns well with earlier assignments, particularly the **use case diagrams** and **state diagrams** developed in previous tasks. For instance, the `Appointment` class corresponds directly to core use cases like “Book Appointment,” “Cancel Appointment,” and “Reschedule Appointment.” Each method within the `Appointment` class maps cleanly to these use cases, and the associated states (e.g., `Pending`, `Confirmed`, `Cancelled`) were reflected in the **state transition diagrams**.
Moreover, the inclusion of classes like `Payment` and `Notification` links back to requirements about user feedback and financial transactions, ensuring traceability to **functional requirements (Assignment 4)** and **sprint tasks (Assignment 6)**. The class diagram helps visualize how the system supports key user interactions described earlier.

## 3. Trade-offs and Design Decisions

Several trade-offs had to be made during the design process. One major decision involved avoiding the use of **inheritance** in favor of **composition** and **association**. For instance, instead of having `Patient` and `Provider` inherit from a common `Person` class, I treated them as separate entities with distinct roles and responsibilities. This kept the model simpler and avoided overcomplicating the inheritance hierarchy, which was not necessary for this relatively small system.
Another trade-off involved **not modeling every possible interaction or helper class**, such as session management, logging, or authentication tokens. These were omitted for clarity and to maintain focus on the main business logic. Such components could be added in a more detailed or implementation-level model.

## 4. Lessons Learned About Object-Oriented Design

This exercise reinforced several core lessons about object-oriented design. First, I learned the importance of **encapsulation**—keeping each class responsible for its own data and behavior, which improves maintainability and clarity. I also gained a deeper appreciation for **modularity**, where well-defined interfaces and responsibilities reduce coupling and make the system easier to extend or refactor.
Additionally, working with **relationships and multiplicities** helped me understand how to model real-world interactions in a way that a development team can translate into actual code. I now see the value in clearly defining associations and ensuring they match user needs and workflow logic.
Overall, this assignment strengthened my ability to think systematically about design and gave me practical experience in translating user needs into a structured and scalable software model.
