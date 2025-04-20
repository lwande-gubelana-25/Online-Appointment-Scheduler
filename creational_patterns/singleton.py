class AppointmentManager:
    _instance = None
    _appointments = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._appointments = []
        return cls._instance

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    def list_appointments(self):
        return self._appointments

# Demo
if __name__ == "__main__":
    mgr1 = AppointmentManager()
    mgr2 = AppointmentManager()
    mgr1.add_appointment("Dental Checkup")

    print(mgr2.list_appointments())  # Should show same data as mgr1
    print("Same instance:", mgr1 is mgr2)
