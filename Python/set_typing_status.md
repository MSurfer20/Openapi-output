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
    op = "start" # str | Whether the user has started (`start`) or stopped (`stop`) to type. 
    to =  # [int] | For 'private' type it is the user_ids of the recipients of the message being typed. Send a JSON-encoded list of user_ids. (Use a list even if there is only one recipient.)  For 'stream' type it is a single element list containing ID of stream in which the message is being typed.  **Changes**: Before Zulip 2.0, this parameter accepted only a JSON-encoded list of email addresses.  Support for the email address-based format was removed in Zulip 3.0 (feature level 11). 
    type = "private" # str | Type of the message being composed.  (optional) if omitted the server will use the default value of "private"
    topic = "typing notifications" # str | Topic to which message is being typed. Required for the 'stream' type. Ignored in case of 'private' type.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set \"typing\" status
        api_response = api_instance.set_typing_status(op, to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->set_typing_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set \"typing\" status
        api_response = api_instance.set_typing_status(op, to, type=type, topic=topic)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->set_typing_status: %s\n" % e)
```


