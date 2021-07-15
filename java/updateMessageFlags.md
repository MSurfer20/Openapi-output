### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    List<Integer> messages = Arrays.asList(); // List<Integer> | An array containing the IDs of the target messages. 
    String op = "add"; // String | Whether to `add` the flag or `remove` it. 
    String flag = "read"; // String | The flag that should be added/removed. 
    try {
      JsonSuccessBase result = apiInstance.updateMessageFlags(messages, op, flag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#updateMessageFlags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

