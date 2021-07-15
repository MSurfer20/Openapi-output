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
    topic = "dinner" # str | The topic to (un)mute. Note that the request will succeed regardless of whether any messages have been sent to the specified topic. 
    op = "add" # str | Whether to mute (`add`) or unmute (`remove`) the provided topic. 
    stream = "Denmark" # str | The name of the stream to access.  (optional)
    stream_id = 42 # int | The ID of the stream to access.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Topic muting
        api_response = api_instance.mute_topic(topic, op)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->mute_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Topic muting
        api_response = api_instance.mute_topic(topic, op, stream=stream, stream_id=stream_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->mute_topic: %s\n" % e)
```


