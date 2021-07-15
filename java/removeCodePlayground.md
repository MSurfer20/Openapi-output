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
    Integer playgroundId = 1; // Integer | The ID of the playground that you want to remove. 
    try {
      JsonSuccess result = apiInstance.removeCodePlayground(playgroundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAndOrganizationsApi#removeCodePlayground");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

