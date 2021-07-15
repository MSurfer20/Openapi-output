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
    filter_id = 2 # int | The ID of the linkifier that you want to update. 
    pattern = "#(?P<id>[0-9]+)" # str | The [Python regular expression](https://docs.python.org/3/howto/regex.html) that should trigger the linkifier. 
    url_format_string = "https://github.com/zulip/zulip/issues/%(id)s" # str | The URL used for the link. If you used named groups for the `pattern`, you can insert their content here with `%(name_of_the_capturing_group)s`. 

    # example passing only required values which don't have defaults set
    try:
        # Update a linkifier
        api_response = api_instance.update_linkifier(filter_id, pattern, url_format_string)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerAndOrganizationsApi->update_linkifier: %s\n" % e)
```


