### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String op = "start"; // String | Whether the user has started (`start`) or stopped (`stop`) to type. 
    List<Integer> to = Arrays.asList(); // List<Integer> | For 'private' type it is the user_ids of the recipients of the message being typed. Send a JSON-encoded list of user_ids. (Use a list even if there is only one recipient.)  For 'stream' type it is a single element list containing ID of stream in which the message is being typed.  **Changes**: Before Zulip 2.0, this parameter accepted only a JSON-encoded list of email addresses.  Support for the email address-based format was removed in Zulip 3.0 (feature level 11). 
    String type = "private"; // String | Type of the message being composed. 
    String topic = "typing notifications"; // String | Topic to which message is being typed. Required for the 'stream' type. Ignored in case of 'private' type. 
    try {
      JsonSuccess result = apiInstance.setTypingStatus(op, to, type, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#setTypingStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

