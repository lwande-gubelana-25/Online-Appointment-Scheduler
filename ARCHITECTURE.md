```mermaid
Graph TD
    Person(patient, "Patient", "A user who books appointments.")
    Person(doctor, "Doctor", "A healthcare provider who manages appointments.")
    System(appointmentSystem, "Appointment Scheduling System", "Manages appointments online.")

    Rel(patient, appointmentSystem, "Books appointments")
    Rel(doctor, appointmentSystem, "Manages schedules")
