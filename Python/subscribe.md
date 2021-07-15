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
    subscriptions =  # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | A list of dictionaries containing the key `name` and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created. The description of the stream created can be specified by setting the dictionary key `description` with an appropriate value. 
    principals =  # [dict] | A list of user ids (preferred) or Zulip display email addresses of the users to be subscribed to or unsubscribed from the streams specified in the `subscriptions` parameter. If not provided, then the requesting user/bot is subscribed.  **Changes**: The integer format is new in Zulip 3.0 (feature level 9).  (optional)
    authorization_errors_fatal = False # bool | A boolean specifying whether authorization errors (such as when the requesting user is not authorized to access a private stream) should be considered fatal or not. When `True`, an authorization error is reported as such. When set to `False`, the response will be a 200 and any streams where the request encountered an authorization error will be listed in the `unauthorized` key.  (optional) if omitted the server will use the default value of True
    announce = True # bool | If one of the streams specified did not exist previously and is thus craeted by this call, this determines whether [notification bot](/help/configure-notification-bot) will send an announcement about the new stream's creation.  (optional) if omitted the server will use the default value of False
    invite_only = True # bool | As described above, this endpoint will create a new stream if passed a stream name that doesn't already exist.  This parameters and the ones that follow are used to request an initial configuration of a created stream; they are ignored for streams that already exist.  This parameter determines whether any newly created streams will be private streams.  (optional) if omitted the server will use the default value of False
    history_public_to_subscribers = False # bool | Whether the stream's message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream.  Corresponds to the [shared history](/help/stream-permissions) option in documentation.  (optional)
    stream_post_policy = 2 # int | Policy for which users can post messages to the stream.  * 1 => Any user can post. * 2 => Only administrators can post. * 3 => Only full members can post. * 4 => Only moderators can post.  **Changes**: New in Zulip 3.0, replacing the previous `is_announcement_only` boolean.  (optional) if omitted the server will use the default value of 1
    message_retention_days =  # dict | Number of days that messages sent to this stream will be stored before being automatically deleted by the [message retention policy](/help/message-retention-policy).  Two special string format values are supported:  * \"realm_default\" => Return to the organization-level setting. * \"forever\" => Retain messages forever.  **Changes**: New in Zulip 3.0 (feature level 17).  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Subscribe to a stream
        api_response = api_instance.subscribe(subscriptions)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->subscribe: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Subscribe to a stream
        api_response = api_instance.subscribe(subscriptions, principals=principals, authorization_errors_fatal=authorization_errors_fatal, announce=announce, invite_only=invite_only, history_public_to_subscribers=history_public_to_subscribers, stream_post_policy=stream_post_policy, message_retention_days=message_retention_days)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->subscribe: %s\n" % e)
```


