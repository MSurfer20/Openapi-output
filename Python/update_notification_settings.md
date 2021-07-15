### Example

```python
import time
import openapi_client
from openapi_client.api import users_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    enable_stream_desktop_notifications = True # bool | Enable visual desktop notifications for stream messages.  (optional)
    enable_stream_email_notifications = True # bool | Enable email notifications for stream messages.  (optional)
    enable_stream_push_notifications = True # bool | Enable mobile notifications for stream messages.  (optional)
    enable_stream_audible_notifications = True # bool | Enable audible desktop notifications for stream messages.  (optional)
    notification_sound = "ding" # str | Notification sound name.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63).  (optional)
    enable_desktop_notifications = True # bool | Enable visual desktop notifications for private messages and @-mentions.  (optional)
    enable_sounds = True # bool | Enable audible desktop notifications for private messages and @-mentions.  (optional)
    enable_offline_email_notifications = True # bool | Enable email notifications for private messages and @-mentions received when the user is offline.  (optional)
    enable_offline_push_notifications = True # bool | Enable mobile notification for private messages and @-mentions received when the user is offline.  (optional)
    enable_online_push_notifications = True # bool | Enable mobile notification for private messages and @-mentions received when the user is online.  (optional)
    enable_digest_emails = True # bool | Enable digest emails when the user is away.  (optional)
    enable_marketing_emails = True # bool | Enable marketing emails. Has no function outside Zulip Cloud.  (optional)
    enable_login_emails = True # bool | Enable email notifications for new logins to account.  (optional)
    message_content_in_email_notifications = True # bool | Include the message's content in email notifications for new messages.  (optional)
    pm_content_in_desktop_notifications = True # bool | Include content of private messages in desktop notifications.  (optional)
    wildcard_mentions_notify = True # bool | Whether wildcard mentions (E.g. @**all**) should send notifications like a personal mention.  (optional)
    desktop_icon_count_display =  # int | Unread count summary (appears in desktop sidebar and browser tab)  * 1 - All unreads * 2 - Private messages and mentions * 3 - None  (optional)
    realm_name_in_notifications = True # bool | Include organization name in subject of message notification emails.  (optional)
    presence_enabled = True # bool | Display the presence status to other users when online.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update notification settings
        api_response = api_instance.update_notification_settings(enable_stream_desktop_notifications=enable_stream_desktop_notifications, enable_stream_email_notifications=enable_stream_email_notifications, enable_stream_push_notifications=enable_stream_push_notifications, enable_stream_audible_notifications=enable_stream_audible_notifications, notification_sound=notification_sound, enable_desktop_notifications=enable_desktop_notifications, enable_sounds=enable_sounds, enable_offline_email_notifications=enable_offline_email_notifications, enable_offline_push_notifications=enable_offline_push_notifications, enable_online_push_notifications=enable_online_push_notifications, enable_digest_emails=enable_digest_emails, enable_marketing_emails=enable_marketing_emails, enable_login_emails=enable_login_emails, message_content_in_email_notifications=message_content_in_email_notifications, pm_content_in_desktop_notifications=pm_content_in_desktop_notifications, wildcard_mentions_notify=wildcard_mentions_notify, desktop_icon_count_display=desktop_icon_count_display, realm_name_in_notifications=realm_name_in_notifications, presence_enabled=presence_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_notification_settings: %s\n" % e)
```


