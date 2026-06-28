from abc import ABC, abstractmethod


class IObserverNotification(ABC):

    @abstractmethod
    def update(self, message: str):
        pass


class ConsoleNotifier(IObserverNotification):
    def update(self, message: str):
        print(f"Notification: {message}")