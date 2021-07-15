### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    StreamsApi apiInstance = new StreamsApi(defaultClient);
    String topic = "dinner"; // String | The topic to (un)mute. Note that the request will succeed regardless of whether any messages have been sent to the specified topic. 
    String op = "add"; // String | Whether to mute (`add`) or unmute (`remove`) the provided topic. 
    String stream = "Denmark"; // String | The name of the stream to access. 
    Integer streamId = 42; // Integer | The ID of the stream to access. 
    try {
      JsonSuccess result = apiInstance.muteTopic(topic, op, stream, streamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamsApi#muteTopic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

