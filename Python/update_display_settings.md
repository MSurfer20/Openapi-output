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
    twenty_four_hour_time = True # bool | Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).  (optional)
    dense_mode = True # bool | This setting has no effect at present.  It is reserved for use in controlling the default font size in Zulip.  (optional)
    starred_message_counts = True # bool | Whether clients should display the [number of starred messages](/help/star-a-message#display-the-number-of-starred-messages).  (optional)
    fluid_layout_width = True # bool | Whether to use the [maximum available screen width](/help/enable-full-width-display) for the web app's center panel (message feed, recent topics) on wide screens.  (optional)
    high_contrast_mode = True # bool | This setting is reserved for use to control variations in Zulip's design to help visually impaired users.  (optional)
    color_scheme =  # int | Controls which [color theme](/help/night-mode) to use.  * 1 - Automatic * 2 - Night mode * 3 - Day mode  Automatic detection is implementing using the standard `prefers-color-scheme` media query.  (optional)
    translate_emoticons = True # bool | Whether to [translate emoticons to emoji](/help/enable-emoticon-translations) in messages the user sends.  (optional)
    default_language = "en" # str | What [default language](/help/change-your-language) to use for the account.  This controls both the Zulip UI as well as email notifications sent to the user.  The value needs to be a standard language code that the Zulip server has translation data for; for example, `\"en\"` for English or `\"de\"` for German.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63).  (optional)
    default_view = "all_messages" # str | The [default view](/help/change-default-view) used when opening a new Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.  * \"recent_topics\" - Recent topics view * \"all_messages\" - All messages view  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64).  (optional)
    left_side_userlist = True # bool | Whether the users list on left sidebar in narrow windows.  This feature is not heavily used and is likely to be reworked.  (optional)
    emojiset = "google" # str | The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons), used to display emoji to the user everything they appear in the UI.  * \"google\" - Google modern * \"google-blob\" - Google classic * \"twitter\" - Twitter * \"text\" - Plain text  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64).  (optional)
    demote_inactive_streams =  # int | Whether to [demote inactive streams](/help/manage-inactive-streams) in the left sidebar.  * 1 - Automatic * 2 - Always * 3 - Never  (optional)
    timezone = "Asia/Kolkata" # str | The user's [configured timezone](/help/change-your-timezone).  Timezone values supported by the server are served at [/static/generated/timezones.json](/static/generated/timezones.json).  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64).  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update display settings
        api_response = api_instance.update_display_settings(twenty_four_hour_time=twenty_four_hour_time, dense_mode=dense_mode, starred_message_counts=starred_message_counts, fluid_layout_width=fluid_layout_width, high_contrast_mode=high_contrast_mode, color_scheme=color_scheme, translate_emoticons=translate_emoticons, default_language=default_language, default_view=default_view, left_side_userlist=left_side_userlist, emojiset=emojiset, demote_inactive_streams=demote_inactive_streams, timezone=timezone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_display_settings: %s\n" % e)
```


