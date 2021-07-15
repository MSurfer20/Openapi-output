### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    message_id = 42 # int | The target message's ID. 
    emoji_name = "octopus" # str | The target emoji's human-readable name.  To find an emoji's name, hover over a message to reveal three icons on the right, then click the smiley face icon. Images of available reaction emojis appear. Hover over the emoji you want, and note that emoji's text name.  (optional)
    emoji_code = "1f419" # str | A unique identifier, defining the specific emoji codepoint requested, within the namespace of the `reaction_type`.  For most API clients, you won't need this, but it's important for Zulip apps to handle rare corner cases when adding/removing votes on an emoji reaction added previously by another user.  If the existing reaction was added when the Zulip server was using a previous version of the emoji data mapping between Unicode codepoints and human-readable names, sending the `emoji_code` in the data for the original reaction allows the Zulip server to correctly interpret your upvote as an upvote rather than a reaction with a \"diffenent\" emoji.  (optional)
    reaction_type = "unicode_emoji" # str | If an app is adding/removing a vote on an existing reaction, it should pass this parameter using the value the server provided for the existing reaction for specificity.  Supported values:  * `unicode_emoji`: Unicode emoji (`emoji_code` will be its Unicode codepoint). * `realm_emoji`: Custom emoji. (`emoji_code` will be its ID). * `zulip_extra_emoji`: Special emoji included with Zulip.  Exists to    namespace the `zulip` emoji.  **Changes**: In Zulip 3.0 (feature level 2), this become optional for [custom emoji](/help/add-custom-emoji); previously, this endpoint assumed `unicode_emoji` if this parameter was not specified.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove an emoji reaction
        api_response = api_instance.remove_reaction(message_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->remove_reaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove an emoji reaction
        api_response = api_instance.remove_reaction(message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->remove_reaction: %s\n" % e)
```


