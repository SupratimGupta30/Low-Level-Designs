from abc import ABC, abstractmethod
from notification import Notification


class INotificationChannel(ABC):
    @abstractmethod
    def send_notification(self, notification: Notification):
        pass