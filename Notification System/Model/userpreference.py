from typing import Set
from channeltype import ChannelType



class UserPreference:
    def __init__(self, user_id: str, preferred_channels: Set['ChannelType']):
        self._user_id = user_id
        self._preferred_channels = preferred_channels

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def preferred_channels(self) -> Set['ChannelType']:
        return self._preferred_channels