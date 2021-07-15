### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $enable_stream_desktop_notifications = true; # boolean | Enable visual desktop notifications for stream messages. 
my $enable_stream_email_notifications = true; # boolean | Enable email notifications for stream messages. 
my $enable_stream_push_notifications = true; # boolean | Enable mobile notifications for stream messages. 
my $enable_stream_audible_notifications = true; # boolean | Enable audible desktop notifications for stream messages. 
my $notification_sound = ding; # string | Notification sound name.  **Changes**: Removed unnecessary JSON-encoding of parameter in Zulip 4.0 (feature level 63). 
my $enable_desktop_notifications = true; # boolean | Enable visual desktop notifications for private messages and @-mentions. 
my $enable_sounds = true; # boolean | Enable audible desktop notifications for private messages and @-mentions. 
my $enable_offline_email_notifications = true; # boolean | Enable email notifications for private messages and @-mentions received when the user is offline. 
my $enable_offline_push_notifications = true; # boolean | Enable mobile notification for private messages and @-mentions received when the user is offline. 
my $enable_online_push_notifications = true; # boolean | Enable mobile notification for private messages and @-mentions received when the user is online. 
my $enable_digest_emails = true; # boolean | Enable digest emails when the user is away. 
my $enable_marketing_emails = true; # boolean | Enable marketing emails. Has no function outside Zulip Cloud. 
my $enable_login_emails = true; # boolean | Enable email notifications for new logins to account. 
my $message_content_in_email_notifications = true; # boolean | Include the message's content in email notifications for new messages. 
my $pm_content_in_desktop_notifications = true; # boolean | Include content of private messages in desktop notifications. 
my $wildcard_mentions_notify = true; # boolean | Whether wildcard mentions (E.g. @**all**) should send notifications like a personal mention. 
my $desktop_icon_count_display = 56; # int | Unread count summary (appears in desktop sidebar and browser tab)  * 1 - All unreads * 2 - Private messages and mentions * 3 - None 
my $realm_name_in_notifications = true; # boolean | Include organization name in subject of message notification emails. 
my $presence_enabled = true; # boolean | Display the presence status to other users when online. 

eval { 
    my $result = $api_instance->update_notification_settings(enable_stream_desktop_notifications => $enable_stream_desktop_notifications, enable_stream_email_notifications => $enable_stream_email_notifications, enable_stream_push_notifications => $enable_stream_push_notifications, enable_stream_audible_notifications => $enable_stream_audible_notifications, notification_sound => $notification_sound, enable_desktop_notifications => $enable_desktop_notifications, enable_sounds => $enable_sounds, enable_offline_email_notifications => $enable_offline_email_notifications, enable_offline_push_notifications => $enable_offline_push_notifications, enable_online_push_notifications => $enable_online_push_notifications, enable_digest_emails => $enable_digest_emails, enable_marketing_emails => $enable_marketing_emails, enable_login_emails => $enable_login_emails, message_content_in_email_notifications => $message_content_in_email_notifications, pm_content_in_desktop_notifications => $pm_content_in_desktop_notifications, wildcard_mentions_notify => $wildcard_mentions_notify, desktop_icon_count_display => $desktop_icon_count_display, realm_name_in_notifications => $realm_name_in_notifications, presence_enabled => $presence_enabled);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->update_notification_settings: $@\n";
}
```

