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
    List<Integer> order = Arrays.asList(); // List<Integer> | A list of the IDs of all the custom profile fields defined in this organization, in the desired new order. 
    try {
      JsonSuccess result = apiInstance.reorderCustomProfileFields(order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAndOrganizationsApi#reorderCustomProfileFields");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

