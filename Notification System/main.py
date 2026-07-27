from channeltype import ChannelType
from notificationdispatcher import NotificationDispatcher
from userpreference import UserPreference
from userpreferenceservice import UserPreferenceService


def main():
    # Instantiate the UserPreferenceService
    preference_service = UserPreferenceService()

    # Save a user preference
    # In Python, Set.of(...) becomes a literal set with curly braces {}
    preference_service.save_preference(
        UserPreference(
            user_id="user123",
            channels={ChannelType.EMAIL, ChannelType.SMS}
        )
    )

    # Instantiate the dispatchers and services
    dispatcher = NotificationDispatcher(preference_service)
    #async_notification_service = AsyncNotificationService(dispatcher)
    notification_service = notification_service(dispatcher)


if __name__ == "__main__":
    main()