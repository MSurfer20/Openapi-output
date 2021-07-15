### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerAndOrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    ServerAndOrganizationsApi apiInstance = new ServerAndOrganizationsApi(defaultClient);
    String emojiName = "smile"; // String | The name that should be associated with the uploaded emoji image/gif. The emoji name can only contain letters, numbers, dashes, and spaces. Upper and lower case letters are treated the same, and underscores (_) are treated the same as spaces (consistent with how the Zulip UI handles emoji). 
    File filename = new File("/path/to/file"); // File | 
    try {
      JsonSuccess result = apiInstance.uploadCustomEmoji(emojiName, filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAndOrganizationsApi#uploadCustomEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

