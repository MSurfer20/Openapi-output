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
    Boolean includePublic = true; // Boolean | Include all public streams. 
    Boolean includeWebPublic = false; // Boolean | Include all web public streams. 
    Boolean includeSubscribed = true; // Boolean | Include all streams that the user is subscribed to. 
    Boolean includeAllActive = false; // Boolean | Include all active streams. The user must have administrative privileges to use this parameter. 
    Boolean includeDefault = false; // Boolean | Include all default streams for the user's realm. 
    Boolean includeOwnerSubscribed = false; // Boolean | If the user is a bot, include all streams that the bot's owner is subscribed to. 
    try {
      JsonSuccessBase result = apiInstance.getStreams(includePublic, includeWebPublic, includeSubscribed, includeAllActive, includeDefault, includeOwnerSubscribed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamsApi#getStreams");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

