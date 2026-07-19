from channeltype import ChannelType
from userpreference import UserPreference
from userpreferenceservice import UserPreferenceService
from notificationchannelfactory import NotificationChannelFactory, get_channel

class NotificationDispatcher:
    def __init__(self, preference_service: UserPreferenceService):
        self.preference_service = preference_service


    def dispatch_notification(self, user_id: str, message: str):
        user_preference = self.preference_service.get_preference(user_id)
        
        for channel_type in user_preference.preferred_channels:
            channel = get_channel(channel_type)
            channel.send_notification(user_id, message)