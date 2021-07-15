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
    List<String> subscriptions = Arrays.asList(); // List<String> | A list of stream names to unsubscribe from. This parameter is called `streams` in our Python API. 
    List<OneOfstringinteger> principals = Arrays.asList(); // List<OneOfstringinteger> | A list of user ids (preferred) or Zulip display email addresses of the users to be subscribed to or unsubscribed from the streams specified in the `subscriptions` parameter. If not provided, then the requesting user/bot is subscribed.  **Changes**: The integer format is new in Zulip 3.0 (feature level 9). 
    try {
      JsonSuccessBase result = apiInstance.unsubscribe(subscriptions, principals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamsApi#unsubscribe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

