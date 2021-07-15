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
    content = "Hello" # str | The content of the message. Maximum message size of 10000 bytes. 

    # example passing only required values which don't have defaults set
    try:
        # Render message
        api_response = api_instance.render_message(content)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->render_message: %s\n" % e)
```


