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
    subscriptions =  # [str] | A list of stream names to unsubscribe from. This parameter is called `streams` in our Python API. 
    principals =  # [dict] | A list of user ids (preferred) or Zulip display email addresses of the users to be subscribed to or unsubscribed from the streams specified in the `subscriptions` parameter. If not provided, then the requesting user/bot is subscribed.  **Changes**: The integer format is new in Zulip 3.0 (feature level 9).  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe from a stream
        api_response = api_instance.unsubscribe(subscriptions)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->unsubscribe: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unsubscribe from a stream
        api_response = api_instance.unsubscribe(subscriptions, principals=principals)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->unsubscribe: %s\n" % e)
```


