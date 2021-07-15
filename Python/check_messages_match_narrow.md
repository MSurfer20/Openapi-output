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
    msg_ids =  # [int] | List of IDs for the messages to check.
    narrow =  # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | A structure defining the narrow to check against. See how to [construct a narrow](/api/construct-narrow).

    # example passing only required values which don't have defaults set
    try:
        # Check if messages match a narrow
        api_response = api_instance.check_messages_match_narrow(msg_ids, narrow)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->check_messages_match_narrow: %s\n" % e)
```


