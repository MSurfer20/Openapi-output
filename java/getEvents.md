### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    RealTimeEventsApi apiInstance = new RealTimeEventsApi(defaultClient);
    String queueId = "1375801870:2942"; // String | The ID of an event queue that was previously registered via `POST /api/v1/register` (see [Register a queue](/api/register-queue)). 
    Integer lastEventId = -1; // Integer | The highest event ID in this queue that you've received and wish to acknowledge. See the [code for `call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/master/zulip/zulip/__init__.py) in the [zulip Python module](https://github.com/zulip/python-zulip-api) for an example implementation of correctly processing each event exactly once. 
    Boolean dontBlock = false; // Boolean | Set to `true` if the client is requesting a nonblocking reply. If not specified, the request will block until either a new event is available or a few minutes have passed, in which case the server will send the client a heartbeat event. 
    try {
      JsonSuccessBase result = apiInstance.getEvents(queueId, lastEventId, dontBlock);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeEventsApi#getEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

