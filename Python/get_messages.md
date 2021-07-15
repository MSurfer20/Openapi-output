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
    num_before = 4 # int | The number of messages with IDs less than the anchor to retrieve. 
    num_after = 8 # int | The number of messages with IDs greater than the anchor to retrieve. 
    anchor =  # dict | Integer message ID to anchor fetching of new messages. Supports special string values for when the client wants the server to compute the anchor to use:  * `newest`: The most recent message. * `oldest`: The oldest message. * `first_unread`: The oldest unread message matching the   query, if any; otherwise, the most recent message.  The special values of `'newest'` and `'oldest'` are also supported for anchoring the query at the most recent or oldest messages.  **Changes**: String values are new in Zulip 3.0 (feature level 1).  The   `first_unread` functionality was supported in Zulip 2.1.x   and older by not sending anchor and using use_first_unread_anchor.    In Zulip 2.1.x and older, `oldest` can be emulated with   `anchor=0`, and `newest` with `anchor=10000000000000000`   (that specific large value works around a bug in Zulip   2.1.x and older in the `found_newest` return value).  (optional)
    narrow =  # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | The narrow where you want to fetch the messages from. See how to [construct a narrow](/api/construct-narrow).  (optional) if omitted the server will use the default value of []
    client_gravatar = True # bool | Whether the client supports computing gravatars URLs.  If enabled, `avatar_url` will be included in the response only if there is a Zulip avatar, and will be `null` for users who are using gravatar as their avatar.  This option significantly reduces the compressed size of user data, since gravatar URLs are long, random strings and thus do not compress well. The `client_gravatar` field is set to `true` if clients can compute their own gravatars.  (optional) if omitted the server will use the default value of False
    apply_markdown = False # bool | If `true`, message content is returned in the rendered HTML format. If `false`, message content is returned in the raw Markdown-format text that user entered.  (optional) if omitted the server will use the default value of True
    use_first_unread_anchor = True # bool | Legacy way to specify `anchor=\"first_unread\"` in Zulip 2.1.x and older.  Whether to use the (computed by the server) first unread message matching the narrow as the `anchor`.  Mutually exclusive with `anchor`.  **Changes**: Deprecated in Zulip 3.0, replaced by `anchor=\"first_unread\"` instead.  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get messages
        api_response = api_instance.get_messages(num_before, num_after)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->get_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get messages
        api_response = api_instance.get_messages(num_before, num_after, anchor=anchor, narrow=narrow, client_gravatar=client_gravatar, apply_markdown=apply_markdown, use_first_unread_anchor=use_first_unread_anchor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->get_messages: %s\n" % e)
```


