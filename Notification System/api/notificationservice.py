from notification import Notification
from notificationdispatcher import NotificationDispatcher

class NotificationService:
    def __init__(self, dispatcher: NotificationDispatcher):
        self.dispatcher = dispatcher

    def send_notification(self, notification: Notification):
        self.dispatcher.dispatch(notification)