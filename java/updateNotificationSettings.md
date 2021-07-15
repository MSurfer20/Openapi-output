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
    Boolean enableStreamDesktopNotifications = true; // Boolean | Enable visual desktop notifications for stream messages. 
    Boolean enableStreamEmailNotifications = true; // Boolean | Enable email notifications for stream messages. 
    Boolean enableStreamPushNotifications = true; // Boolean | Enable mobile notifications for stream messages. 
    Boolean enableStreamAudibleNotifications = true; // Boolean | Enable audible desktop notifications for stream messages. 
    String notificationSound = "ding"; // String | Notification sound name.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63). 
    Boolean enableDesktopNotifications = true; // Boolean | Enable visual desktop notifications for private messages and @-mentions. 
    Boolean enableSounds = true; // Boolean | Enable audible desktop notifications for private messages and @-mentions. 
    Boolean enableOfflineEmailNotifications = true; // Boolean | Enable email notifications for private messages and @-mentions received when the user is offline. 
    Boolean enableOfflinePushNotifications = true; // Boolean | Enable mobile notification for private messages and @-mentions received when the user is offline. 
    Boolean enableOnlinePushNotifications = true; // Boolean | Enable mobile notification for private messages and @-mentions received when the user is online. 
    Boolean enableDigestEmails = true; // Boolean | Enable digest emails when the user is away. 
    Boolean enableMarketingEmails = true; // Boolean | Enable marketing emails. Has no function outside Zulip Cloud. 
    Boolean enableLoginEmails = true; // Boolean | Enable email notifications for new logins to account. 
    Boolean messageContentInEmailNotifications = true; // Boolean | Include the message's content in email notifications for new messages. 
    Boolean pmContentInDesktopNotifications = true; // Boolean | Include content of private messages in desktop notifications. 
    Boolean wildcardMentionsNotify = true; // Boolean | Whether wildcard mentions (E.g. @**all**) should send notifications like a personal mention. 
    Integer desktopIconCountDisplay = 56; // Integer | Unread count summary (appears in desktop sidebar and browser tab)  * 1 - All unreads * 2 - Private messages and mentions * 3 - None 
    Boolean realmNameInNotifications = true; // Boolean | Include organization name in subject of message notification emails. 
    Boolean presenceEnabled = true; // Boolean | Display the presence status to other users when online. 
    try {
      JsonSuccessBase result = apiInstance.updateNotificationSettings(enableStreamDesktopNotifications, enableStreamEmailNotifications, enableStreamPushNotifications, enableStreamAudibleNotifications, notificationSound, enableDesktopNotifications, enableSounds, enableOfflineEmailNotifications, enableOfflinePushNotifications, enableOnlinePushNotifications, enableDigestEmails, enableMarketingEmails, enableLoginEmails, messageContentInEmailNotifications, pmContentInDesktopNotifications, wildcardMentionsNotify, desktopIconCountDisplay, realmNameInNotifications, presenceEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateNotificationSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

