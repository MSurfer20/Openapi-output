### Example

```python
import time
import openapi_client
from openapi_client.api import server_and_organizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = server_and_organizations_api.ServerAndOrganizationsApi(api_client)
    order =  # [int] | A list of the IDs of all the custom profile fields defined in this organization, in the desired new order. 

    # example passing only required values which don't have defaults set
    try:
        # Reorder custom profile fields
        api_response = api_instance.reorder_custom_profile_fields(order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerAndOrganizationsApi->reorder_custom_profile_fields: %s\n" % e)
```


