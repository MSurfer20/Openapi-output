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
    messages =  # [int] | An array containing the IDs of the target messages. 
    op = "add" # str | Whether to `add` the flag or `remove` it. 
    flag = "read" # str | The flag that should be added/removed. 

    # example passing only required values which don't have defaults set
    try:
        # Update personal message flags
        api_response = api_instance.update_message_flags(messages, op, flag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->update_message_flags: %s\n" % e)
```


