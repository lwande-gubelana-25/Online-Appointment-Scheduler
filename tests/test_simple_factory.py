from tests.factories.simple_factory import NotificationFactory

class NotificationFactory:
    def create_notification(self, type):
        if type == "email":
            return Email the corrected version:

```python
from tests.factNotification()
        elif type == "sms":
            return SMSNotification()
        elseories.simple_factory import NotificationFactory
``:
            raise ValueError(f"Unknown notification type: {type}")
