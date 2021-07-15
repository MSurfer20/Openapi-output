### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "iago@zulip.com"; // String | The username to be used for authentication (typically, the email address, but depending on configuration, it could be an LDAP username).  See the `require_email_format_usernames` parameter documented in [GET /server_settings](/api/get-server-settings) for details. 
    String password = "abcd1234"; // String | The user's Zulip password (or LDAP password, if LDAP authentication is in use). 
    try {
      ApiKeyResponse result = apiInstance.fetchApiKey(username, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#fetchApiKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

