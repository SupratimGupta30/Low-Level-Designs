from channeltype import ChannelType
from typing import Optional

class Notification:
    def __init__(self, user_id: str, message: str):
        self._user_id = user_id        # "Private" by convention
        self._message = message        # "Private" by convention
        self._type: Optional[ChannelType] = None

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def message(self) -> str:
        return self._message

    @property
    def type(self) -> Optional[ChannelType]:
        return self._type

    @type.setter
    def type(self, channel_type: ChannelType):
        self._type = channel_type