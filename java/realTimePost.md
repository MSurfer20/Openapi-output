### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    RealTimeEventsApi apiInstance = new RealTimeEventsApi(defaultClient);
    List<String> eventTypes = Arrays.asList(); // List<String> | A JSON-encoded array indicating which types of events you're interested in. Values that you might find useful include:    * **message** (messages)   * **subscription** (changes in your subscriptions)   * **realm_user** (changes to users in the organization and     their properties, such as their name).  If you do not specify this parameter, you will receive all events, and have to filter out the events not relevant to your client in your client code.  For most applications, one is only interested in messages, so one specifies: `event_types=['message']`  Event types not supported by the server are ignored, in order to simplify the implementation of client apps that support multiple server versions. 
    List<List<String>> narrow = Arrays.asList(new ArrayList<String>()); // List<List<String>> | A JSON-encoded array of arrays of length 2 indicating the narrow for which you'd like to receive events for. For instance, to receive events for the stream `Denmark`, you would specify `narrow=[['stream', 'Denmark']]`.  Another example is `narrow=[['is', 'private']]` for private messages. Default is `[]`. 
    Boolean allPublicStreams = false; // Boolean | Whether you would like to request message events from all public streams.  Useful for workflow bots that you'd like to see all new messages sent to public streams.  (You can also subscribe the user to private streams). 
    try {
      apiInstance.realTimePost(eventTypes, narrow, allPublicStreams);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeEventsApi#realTimePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

