### Example

```python
import time
import openapi_client
from openapi_client.api import webhooks_api
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Outgoing webhooks
        api_response = api_instance.zulip_outgoing_webhooks()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhooksApi->zulip_outgoing_webhooks: %s\n" % e)
```


