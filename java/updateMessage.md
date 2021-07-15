### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.zulipchat.com/api/v1");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer messageId = 42; // Integer | The target message's ID. 
    String topic = "Castle"; // String | The topic to move the message(s) to, to request changing the topic. Should only be sent when changing the topic, and will throw an error if the target message is not a stream message.  Maximum length of 60 characters.  **Changes**: New in Zulip 2.0.  Previous Zulip releases encoded this as `subject`, which is currently a deprecated alias. 
    String propagateMode = "change_one"; // String | Which message(s) should be edited: just the one indicated in `message_id`, messages in the same topic that had been sent after this one, or all of them.  Only the default value of `change_one` is valid when editing only the content of a message.  This parameter determines both which messages get moved and also whether clients that are currently narrowed to the topic containing the message should navigate or adjust their compose box recipient to point to the post-edit stream/topic. 
    Boolean sendNotificationToOldThread = true; // Boolean | Whether to send breadcrumb message to the old thread to notify users where the messages were moved to.  **Changes**: New in Zulip 3.0 (feature level 9). 
    Boolean sendNotificationToNewThread = true; // Boolean | Whether to send a notification message to the new thread to notify users where the messages came from.  **Changes**: New in Zulip 3.0 (feature level 9). 
    String content = "Hello"; // String | The content of the message. Maximum message size of 10000 bytes. 
    Integer streamId = 42; // Integer | The stream ID to move the message(s) to, to request moving messages to another stream.  Should only be sent when changing the stream, and will throw an error if the target message is not a stream message. 
    try {
      JsonSuccess result = apiInstance.updateMessage(messageId, topic, propagateMode, sendNotificationToOldThread, sendNotificationToNewThread, content, streamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#updateMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

