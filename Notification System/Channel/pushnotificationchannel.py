from notificationchannel import INotificationChannel
from notification import Notification

class PushNotificationChannel(INotificationChannel):
    def send_notification(self, notification: Notification):
        # Implement the logic to send a push notification
        print(f"Sending push notification to User {notification.user_id}: {notification.message}")