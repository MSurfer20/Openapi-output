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
    Integer streamId = 1; // Integer | The ID of the stream to access. 
    String description = "Discuss Italian history and travel destinations."; // String | The new description for the stream. Limited Zulip markdown is allowed in this field.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64). 
    String newName = "Italy"; // String | The new name for the stream.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64). 
    Boolean isPrivate = true; // Boolean | Change whether the stream is a private stream. 
    Boolean isAnnouncementOnly = true; // Boolean | Whether the stream is limited to announcements.  **Changes**: Deprecated in Zulip 3.0 (feature level 1), use   `stream_post_policy` instead. 
    Integer streamPostPolicy = 1; // Integer | Policy for which users can post messages to the stream.  * 1 => Any user can post. * 2 => Only administrators can post. * 3 => Only full members can post. * 4 => Only moderators can post.  **Changes**: New in Zulip 3.0, replacing the previous `is_announcement_only` boolean. 
    Boolean historyPublicToSubscribers = false; // Boolean | Whether the stream's message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream.  Corresponds to the [shared history](/help/stream-permissions) option in documentation. 
    OneOfstringinteger messageRetentionDays = new OneOfstringinteger(); // OneOfstringinteger | Number of days that messages sent to this stream will be stored before being automatically deleted by the [message retention policy](/help/message-retention-policy).  Two special string format values are supported:  * \"realm_default\" => Return to the organization-level setting. * \"forever\" => Retain messages forever.  **Changes**: New in Zulip 3.0 (feature level 17). 
    try {
      JsonSuccess result = apiInstance.updateStream(streamId, description, newName, isPrivate, isAnnouncementOnly, streamPostPolicy, historyPublicToSubscribers, messageRetentionDays);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamsApi#updateStream");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

