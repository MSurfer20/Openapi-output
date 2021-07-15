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
    last_event_id = -1 # int | The highest event ID in this queue that you've received and wish to acknowledge. See the [code for `call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/master/zulip/zulip/__init__.py) in the [zulip Python module](https://github.com/zulip/python-zulip-api) for an example implementation of correctly processing each event exactly once.  (optional)
    dont_block = True # bool | Set to `true` if the client is requesting a nonblocking reply. If not specified, the request will block until either a new event is available or a few minutes have passed, in which case the server will send the client a heartbeat event.  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get events from an event queue
        api_response = api_instance.get_events(queue_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeEventsApi->get_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get events from an event queue
        api_response = api_instance.get_events(queue_id, last_event_id=last_event_id, dont_block=dont_block)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeEventsApi->get_events: %s\n" % e)
```


