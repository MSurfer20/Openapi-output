### Example

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    username = "iago@zulip.com" # str | The email address for the user that owns the API key. 

    # example passing only required values which don't have defaults set
    try:
        # Fetch an API key (development only)
        api_response = api_instance.dev_fetch_api_key(username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->dev_fetch_api_key: %s\n" % e)
```


