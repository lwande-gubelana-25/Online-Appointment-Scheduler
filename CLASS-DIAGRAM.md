# Class Diagram

```mermaid
classDiagram
    class User {
        -userID: String
        -name: String
        -email: String
        -phone: String
        -password: String
        -role: String
        +login()
        +register()
        +updateProfile()
    }

    class Appointment {
        -appointmentID: String
        -dateTime: DateTime
        -status: String
        -reason: String
        +book()
        +cancel()
        +reschedule()
    }

    class Service {
        -serviceID: String
        -name: String
        -description: String
        -duration: int
        -price: float
        +listServices()
        +updateService()
    }

    class Provider {
        -providerID: String
        -name: String
        -specialization: String
        -email: String
        -phone: String
        +viewSchedule()
        +updateAvailability()
    }

    class Schedule {
        -scheduleID: String
        -startTime: DateTime
        -endTime: DateTime
        -isAvailable: Boolean
        +checkAvailability()
        +updateSlot()
    }

    class Payment {
        -paymentID: String
        -amount: float
        -method: String
        -status: String
        -timestamp: DateTime
        +processPayment()
        +refund()
    }

    class Notification {
        -notificationID: String
        -message: String
        -timestamp: DateTime
        -readStatus: Boolean
        +send()
        +markAsRead()
    }

    %% Relationships
    User "1" --> "0..*" Appointment : books
    Appointment "1" --> "1" Service : for
    Appointment "1" --> "1" Provider : with
    Provider "1" --> "1" Schedule : manages
    Appointment "1" --> "1" Payment : includes
    User "1" --> "0..*" Notification : receives
``` 

## Explanation

- User interacts with the system to book and manage appointments.
- Appointment is central, connecting users, services, providers, and payment.
- Service represents various offerings like dental consultation, therapy, etc.
- Provider is the professional offering services (e.g., doctor, therapist).
- Schedule is tightly associated with each provider to track availability.
- Payment handles financial transactions tied to appointments.
- Notification alerts users about appointments and updates.
- Multiplicities (e.g., 1, 0.., 1..) describe how many instances are involved in each relationship.


```mermaid
classDiagram
    class Repository {
        <<interface>>
        +save(entity)
        +find_by_id(id)
        +find_all()
        +delete(id)
    }

    class InMemoryUserRepository {
        +save(user)
        +find_by_id(id)
        +find_all()
        +delete(id)
    }

    class FileSystemUserRepository {
        +save(user)
        +find_by_id(id)
        +find_all()
        +delete(id)
    }

    class DatabaseUserRepository {
        +save(user)
        +find_by_id(id)
        +find_all()
        +delete(id)
    }

    Repository <|-- InMemoryUserRepository
    Repository <|-- FileSystemUserRepository
    Repository <|-- DatabaseUserRepository

