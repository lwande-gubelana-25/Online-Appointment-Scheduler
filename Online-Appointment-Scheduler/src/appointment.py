from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    id: str
    user_id: str
    service: str
    datetime: datetime
