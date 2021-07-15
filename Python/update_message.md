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
    topic = "Castle" # str | The topic to move the message(s) to, to request changing the topic. Should only be sent when changing the topic, and will throw an error if the target message is not a stream message.  Maximum length of 60 characters.  **Changes**: New in Zulip 2.0.  Previous Zulip releases encoded this as `subject`, which is currently a deprecated alias.  (optional)
    propagate_mode = "change_all" # str | Which message(s) should be edited: just the one indicated in `message_id`, messages in the same topic that had been sent after this one, or all of them.  Only the default value of `change_one` is valid when editing only the content of a message.  This parameter determines both which messages get moved and also whether clients that are currently narrowed to the topic containing the message should navigate or adjust their compose box recipient to point to the post-edit stream/topic.  (optional) if omitted the server will use the default value of "change_one"
    send_notification_to_old_thread = True # bool | Whether to send breadcrumb message to the old thread to notify users where the messages were moved to.  **Changes**: New in Zulip 3.0 (feature level 9).  (optional) if omitted the server will use the default value of True
    send_notification_to_new_thread = True # bool | Whether to send a notification message to the new thread to notify users where the messages came from.  **Changes**: New in Zulip 3.0 (feature level 9).  (optional) if omitted the server will use the default value of True
    content = "Hello" # str | The content of the message. Maximum message size of 10000 bytes.  (optional)
    stream_id = 42 # int | The stream ID to move the message(s) to, to request moving messages to another stream.  Should only be sent when changing the stream, and will throw an error if the target message is not a stream message.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a message
        api_response = api_instance.update_message(message_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->update_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a message
        api_response = api_instance.update_message(message_id, topic=topic, propagate_mode=propagate_mode, send_notification_to_old_thread=send_notification_to_old_thread, send_notification_to_new_thread=send_notification_to_new_thread, content=content, stream_id=stream_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->update_message: %s\n" % e)
```


