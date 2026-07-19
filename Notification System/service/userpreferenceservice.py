from channeltype import ChannelType
from userpreference import UserPreference


class UserPreferenceService:

    def __init__(self):
        # We use a standard built-in dictionary to act as our HashMap
        self._preferences: dict[str, UserPreference] = {}

    def save_preference(self, preference: UserPreference) -> None:
        self._preferences[preference.get_user_id()] = preference

    def get_preference(self, user_id: str) -> UserPreference:
        return self._preferences.get(
            user_id, 
            UserPreference(user_id, {ChannelType.EMAIL})
        )