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
    email = "username@example.com" # str | The email address of the new user. 
    password = "abcd1234" # str | The password of the new user. 
    full_name = "New User" # str | The full name of the new user. 

    # example passing only required values which don't have defaults set
    try:
        # Create a user
        api_response = api_instance.create_user(email, password, full_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```


