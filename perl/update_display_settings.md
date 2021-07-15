### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $twenty_four_hour_time = true; # boolean | Whether time should be [displayed in 24-hour notation](/help/change-the-time-format). 
my $dense_mode = true; # boolean | This setting has no effect at present.  It is reserved for use in controlling the default font size in Zulip. 
my $starred_message_counts = true; # boolean | Whether clients should display the [number of starred messages](/help/star-a-message#display-the-number-of-starred-messages). 
my $fluid_layout_width = true; # boolean | Whether to use the [maximum available screen width](/help/enable-full-width-display) for the web app's center panel (message feed, recent topics) on wide screens. 
my $high_contrast_mode = true; # boolean | This setting is reserved for use to control variations in Zulip's design to help visually impaired users. 
my $color_scheme = 56; # int | Controls which [color theme](/help/night-mode) to use.  * 1 - Automatic * 2 - Night mode * 3 - Day mode  Automatic detection is implementing using the standard `prefers-color-scheme` media query. 
my $translate_emoticons = true; # boolean | Whether to [translate emoticons to emoji](/help/enable-emoticon-translations) in messages the user sends. 
my $default_language = en; # string | What [default language](/help/change-your-language) to use for the account.  This controls both the Zulip UI as well as email notifications sent to the user.  The value needs to be a standard language code that the Zulip server has translation data for; for example, `\"en\"` for English or `\"de\"` for German.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63). 
my $default_view = all_messages; # string | The [default view](/help/change-default-view) used when opening a new Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.  * \"recent_topics\" - Recent topics view * \"all_messages\" - All messages view  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 
my $left_side_userlist = true; # boolean | Whether the users list on left sidebar in narrow windows.  This feature is not heavily used and is likely to be reworked. 
my $emojiset = google; # string | The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons), used to display emoji to the user everything they appear in the UI.  * \"google\" - Google modern * \"google-blob\" - Google classic * \"twitter\" - Twitter * \"text\" - Plain text  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 
my $demote_inactive_streams = 56; # int | Whether to [demote inactive streams](/help/manage-inactive-streams) in the left sidebar.  * 1 - Automatic * 2 - Always * 3 - Never 
my $timezone = Asia/Kolkata; # string | The user's [configured timezone](/help/change-your-timezone).  Timezone values supported by the server are served at [/static/generated/timezones.json](/static/generated/timezones.json).  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 64). 

eval { 
    my $result = $api_instance->update_display_settings(twenty_four_hour_time => $twenty_four_hour_time, dense_mode => $dense_mode, starred_message_counts => $starred_message_counts, fluid_layout_width => $fluid_layout_width, high_contrast_mode => $high_contrast_mode, color_scheme => $color_scheme, translate_emoticons => $translate_emoticons, default_language => $default_language, default_view => $default_view, left_side_userlist => $left_side_userlist, emojiset => $emojiset, demote_inactive_streams => $demote_inactive_streams, timezone => $timezone);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->update_display_settings: $@\n";
}
```

