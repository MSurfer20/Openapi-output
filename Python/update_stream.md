### Example

```python
import time
import openapi_client
from openapi_client.api import streams_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    stream_id = 1 # int | The ID of the stream to access. 
    description = "Discuss Italian history and travel destinations." # str | The new description for the stream. Limited Zulip markdown is allowed in this field.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64).  (optional)
    new_name = "Italy" # str | The new name for the stream.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64).  (optional)
    is_private = True # bool | Change whether the stream is a private stream.  (optional)
    is_announcement_only = True # bool | Whether the stream is limited to announcements.  **Changes**: Deprecated in Zulip 3.0 (feature level 1), use   `stream_post_policy` instead.  (optional)
    stream_post_policy = 2 # int | Policy for which users can post messages to the stream.  * 1 => Any user can post. * 2 => Only administrators can post. * 3 => Only full members can post. * 4 => Only moderators can post.  **Changes**: New in Zulip 3.0, replacing the previous `is_announcement_only` boolean.  (optional) if omitted the server will use the default value of 1
    history_public_to_subscribers = False # bool | Whether the stream's message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream.  Corresponds to the [shared history](/help/stream-permissions) option in documentation.  (optional)
    message_retention_days =  # dict | Number of days that messages sent to this stream will be stored before being automatically deleted by the [message retention policy](/help/message-retention-policy).  Two special string format values are supported:  * \"realm_default\" => Return to the organization-level setting. * \"forever\" => Retain messages forever.  **Changes**: New in Zulip 3.0 (feature level 17).  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a stream
        api_response = api_instance.update_stream(stream_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->update_stream: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a stream
        api_response = api_instance.update_stream(stream_id, description=description, new_name=new_name, is_private=is_private, is_announcement_only=is_announcement_only, stream_post_policy=stream_post_policy, history_public_to_subscribers=history_public_to_subscribers, message_retention_days=message_retention_days)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->update_stream: %s\n" % e)
```


