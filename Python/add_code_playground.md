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
    name = "Python playground" # str | The user-visible display name of the playground which can be used to pick the target playground, especially when multiple playground options exist for that programming language. 
    pygments_language = "Python" # str | The name of the Pygments language lexer for that programming language. 
    url_prefix = "https://python.example.com" # str | The url prefix for the playground. 

    # example passing only required values which don't have defaults set
    try:
        # Add a code playground
        api_response = api_instance.add_code_playground(name, pygments_language, url_prefix)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerAndOrganizationsApi->add_code_playground: %s\n" % e)
```


