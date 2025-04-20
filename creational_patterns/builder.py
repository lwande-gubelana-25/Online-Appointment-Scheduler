class Appointment:
    def __init__(self, date_time=None, provider=None, service=None):
        self.date_time = date_time
        self.provider = provider
        self.service = service

class AppointmentBuilder:
    def __init__(self):
        self._appointment = Appointment()

    def set_date_time(self, date_time):
        self._appointment.date_time = date_time
        return self

    def set_provider(self, provider):
        self._appointment.provider = provider
        return self

    def set_service(self, service):
        self._appointment.service = service
        return self

    def build(self):
        return self._appointment

# Demo
if __name__ == "__main__":
    appointment = (
        AppointmentBuilder()
        .set_provider("Dr. Mngambi")
        .set_service("Dental Cleaning")
        .build()
    )
    print(f"Appointment with {appointment.provider} for {appointment.service}")
