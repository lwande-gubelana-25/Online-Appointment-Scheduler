C4Context
  Person(patient, "Patient", "A user who books appointments.")
  Person(doctor, "Doctor", "A healthcare provider who manages appointments.")
  System(appointmentSystem, "Appointment Scheduling System", "Manages appointments online.")
  
  patient -> appointmentSystem : "Book appointments"
  doctor -> appointmentSystem : "Manage schedules"

C4Container
  Person(patient, "Patient")
  Person(doctor, "Doctor")
  System_Boundary(appointmentSystem, "Online Appointment System") {
    Container(webApp, "Web Application", "React", "User interface")
    Container(api, "Backend API", "Node.js", "Handles business logic")
    ContainerDb(db, "Database", "PostgreSQL", "Stores appointments and user data")
  }
  patient -> webApp : "Uses"
  doctor -> webApp : "Uses"
  webApp -> api : "API Calls"
  api -> db : "Reads/Writes"
