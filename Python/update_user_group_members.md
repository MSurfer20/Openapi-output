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
    user_group_id = 1 # int | The ID of the target user group. 
    delete =  # [int] | The list of user ids to be removed from the user group.  (optional)
    add =  # [int] | The list of user ids to be added to the user group.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update user group members
        api_response = api_instance.update_user_group_members(user_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user_group_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update user group members
        api_response = api_instance.update_user_group_members(user_group_id, delete=delete, add=add)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user_group_members: %s\n" % e)
```


