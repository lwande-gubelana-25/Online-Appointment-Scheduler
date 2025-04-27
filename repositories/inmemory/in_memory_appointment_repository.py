from repositories.appointment_repository import AppointmentRepository
from typing import Optional, List
from src.appointment import Appointment

class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self._storage = {}

    def save(self, appointment: Appointment) -> None:
        self._storage[appointment.appointment_id] = appointment

    def find_by_id(self, id: str) -> Optional[Appointment]:
        return self._storage.get(id)

    def find_all(self) -> List[Appointment]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
