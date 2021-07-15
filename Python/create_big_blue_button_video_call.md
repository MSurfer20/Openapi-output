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

    # example, this endpoint has no required or optional parameters
    try:
        # Create BigBlueButton video call
        api_response = api_instance.create_big_blue_button_video_call()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StreamsApi->create_big_blue_button_video_call: %s\n" % e)
```


