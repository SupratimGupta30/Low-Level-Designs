from notificationchannel import INotificationChannel
from notification import Notification

class SMSNotificationChannel(INotificationChannel):
    def send_notification(self, notification: Notification):
        # Implement the logic to send an SMS notification
        print(f"Sending SMS notification to User {notification.user_id}: {notification.message}")