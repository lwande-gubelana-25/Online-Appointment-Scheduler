from repositories.repository import Repository
from src.appointment import Appointment

class AppointmentRepository(Repository[Appointment, str]):
    pass