from emailnotificationchannel import EmailNotificationChannel
from smsnotificationchannel import SmsNotificationChannel
from pushnotificationchannel import PushNotificationChannel
from channeltype import ChannelType

def get_channel(channel_type: ChannelType):
    match channel_type:
        case ChannelType.EMAIL:
            return EmailNotificationChannel()
        case ChannelType.SMS:
            return SmsNotificationChannel()
        case ChannelType.PUSH:
            return PushNotificationChannel()
        case _:
            raise ValueError(f"Unknown channel type: {channel_type}")