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
    stream_id = 42 # int | The ID of the stream to access. 
    topic_name = "new coffee machine" # str | The name of the topic whose messages should be marked as read. 

    # example passing only required values which don't have defaults set
    try:
        # Mark messages in a topic as read
        api_response = api_instance.mark_topic_as_read(stream_id, topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->mark_topic_as_read: %s\n" % e)
```


