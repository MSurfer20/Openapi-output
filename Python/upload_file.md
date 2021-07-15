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
    filename = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a file
        api_response = api_instance.upload_file(filename=filename)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->upload_file: %s\n" % e)
```


