### Example

```python
import time
import openapi_client
from openapi_client.api import real_time_events_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_events_api.RealTimeEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Error handling
        api_instance.rest_error_handling()
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeEventsApi->rest_error_handling: %s\n" % e)
```


