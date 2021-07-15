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
    include_public = False # bool | Include all public streams.  (optional) if omitted the server will use the default value of True
    include_web_public = True # bool | Include all web public streams.  (optional) if omitted the server will use the default value of False
    include_subscribed = False # bool | Include all streams that the user is subscribed to.  (optional) if omitted the server will use the default value of True
    include_all_active = True # bool | Include all active streams. The user must have administrative privileges to use this parameter.  (optional) if omitted the server will use the default value of False
    include_default = True # bool | Include all default streams for the user's realm.  (optional) if omitted the server will use the default value of False
    include_owner_subscribed = True # bool | If the user is a bot, include all streams that the bot's owner is subscribed to.  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all streams
        api_response = api_instance.get_streams(include_public=include_public, include_web_public=include_web_public, include_subscribed=include_subscribed, include_all_active=include_all_active, include_default=include_default, include_owner_subscribed=include_owner_subscribed)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->get_streams: %s\n" % e)
```


