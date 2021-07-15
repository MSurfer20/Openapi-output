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
    queue_id = "1375801870:2942" # str | The ID of an event queue that was previously registered via `POST /api/v1/register` (see [Register a queue](/api/register-queue)). 

    # example passing only required values which don't have defaults set
    try:
        # Delete an event queue
        api_response = api_instance.delete_queue(queue_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeEventsApi->delete_queue: %s\n" % e)
```


