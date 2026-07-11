from notificationchannel import INotificationChannel
from notification import Notification

class EmailNotificationChannel(INotificationChannel):
    def send_notification(self, notification: Notification):
        # Implement the logic to send an email notification
        print(f"Sending email notification to User {notification.user_id}: {notification.message}")