### Example

```python
import time
import openapi_client
from openapi_client.api import users_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    name = "marketing" # str | The name of the user group. 
    description = "The marketing team." # str | The description of the user group. 
    members =  # [int] | An array containing the user IDs of the initial members for the new user group. 

    # example passing only required values which don't have defaults set
    try:
        # Create a user group
        api_response = api_instance.create_user_group(name, description, members)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->create_user_group: %s\n" % e)
```


