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
    delete =  # [str] | A list of stream names to unsubscribe from.  (optional)
    add =  # [dict] | A list of objects describing which streams to subscribe to, optionally including per-user subscription parameters (e.g. color) and if the stream is to be created, its description.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update subscriptions
        api_response = api_instance.update_subscriptions(delete=delete, add=add)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->update_subscriptions: %s\n" % e)
```


