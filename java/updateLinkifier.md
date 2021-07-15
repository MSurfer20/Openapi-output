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
    Integer filterId = 2; // Integer | The ID of the linkifier that you want to update. 
    String pattern = "#(?P<id>[0-9]+)"; // String | The [Python regular expression](https://docs.python.org/3/howto/regex.html) that should trigger the linkifier. 
    String urlFormatString = "https://github.com/zulip/zulip/issues/%(id)s"; // String | The URL used for the link. If you used named groups for the `pattern`, you can insert their content here with `%(name_of_the_capturing_group)s`. 
    try {
      JsonSuccess result = apiInstance.updateLinkifier(filterId, pattern, urlFormatString);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAndOrganizationsApi#updateLinkifier");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

