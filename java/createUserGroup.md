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
    String name = "marketing"; // String | The name of the user group. 
    String description = "The marketing team."; // String | The description of the user group. 
    List<Integer> members = Arrays.asList(); // List<Integer> | An array containing the user IDs of the initial members for the new user group. 
    try {
      JsonSuccess result = apiInstance.createUserGroup(name, description, members);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createUserGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

