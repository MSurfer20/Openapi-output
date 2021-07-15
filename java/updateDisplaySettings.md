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
    Boolean twentyFourHourTime = true; // Boolean | Whether time should be [displayed in 24-hour notation](/help/change-the-time-format). 
    Boolean denseMode = true; // Boolean | This setting has no effect at present.  It is reserved for use in controlling the default font size in Zulip. 
    Boolean starredMessageCounts = true; // Boolean | Whether clients should display the [number of starred messages](/help/star-a-message#display-the-number-of-starred-messages). 
    Boolean fluidLayoutWidth = true; // Boolean | Whether to use the [maximum available screen width](/help/enable-full-width-display) for the web app's center panel (message feed, recent topics) on wide screens. 
    Boolean highContrastMode = true; // Boolean | This setting is reserved for use to control variations in Zulip's design to help visually impaired users. 
    Integer colorScheme = 56; // Integer | Controls which [color theme](/help/night-mode) to use.  * 1 - Automatic * 2 - Night mode * 3 - Day mode  Automatic detection is implementing using the standard `prefers-color-scheme` media query. 
    Boolean translateEmoticons = true; // Boolean | Whether to [translate emoticons to emoji](/help/enable-emoticon-translations) in messages the user sends. 
    String defaultLanguage = "en"; // String | What [default language](/help/change-your-language) to use for the account.  This controls both the Zulip UI as well as email notifications sent to the user.  The value needs to be a standard language code that the Zulip server has translation data for; for example, `\"en\"` for English or `\"de\"` for German.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63). 
    String defaultView = "all_messages"; // String | The [default view](/help/change-default-view) used when opening a new Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.  * \"recent_topics\" - Recent topics view * \"all_messages\" - All messages view  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 
    Boolean leftSideUserlist = true; // Boolean | Whether the users list on left sidebar in narrow windows.  This feature is not heavily used and is likely to be reworked. 
    String emojiset = "google"; // String | The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons), used to display emoji to the user everything they appear in the UI.  * \"google\" - Google modern * \"google-blob\" - Google classic * \"twitter\" - Twitter * \"text\" - Plain text  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 
    Integer demoteInactiveStreams = 56; // Integer | Whether to [demote inactive streams](/help/manage-inactive-streams) in the left sidebar.  * 1 - Automatic * 2 - Always * 3 - Never 
    String timezone = "Asia/Kolkata"; // String | The user's [configured timezone](/help/change-your-timezone).  Timezone values supported by the server are served at [/static/generated/timezones.json](/static/generated/timezones.json).  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 
    try {
      JsonSuccessBase result = apiInstance.updateDisplaySettings(twentyFourHourTime, denseMode, starredMessageCounts, fluidLayoutWidth, highContrastMode, colorScheme, translateEmoticons, defaultLanguage, defaultView, leftSideUserlist, emojiset, demoteInactiveStreams, timezone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateDisplaySettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

