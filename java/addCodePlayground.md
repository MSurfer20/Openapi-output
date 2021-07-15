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
    String name = "Python playground"; // String | The user-visible display name of the playground which can be used to pick the target playground, especially when multiple playground options exist for that programming language. 
    String pygmentsLanguage = "Python"; // String | The name of the Pygments language lexer for that programming language. 
    String urlPrefix = "https://python.example.com"; // String | The url prefix for the playground. 
    try {
      JsonSuccessBase result = apiInstance.addCodePlayground(name, pygmentsLanguage, urlPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAndOrganizationsApi#addCodePlayground");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

