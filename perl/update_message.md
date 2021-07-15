### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $message_id = 42; # int | The target message's ID. 
my $topic = Castle; # string | The topic to move the message(s) to, to request changing the topic. Should only be sent when changing the topic, and will throw an error if the target message is not a stream message.  Maximum length of 60 characters.  **Changes**: New in Zulip 2.0.  Previous Zulip releases encoded this as `subject`, which is currently a deprecated alias. 
my $propagate_mode = change_all; # string | Which message(s) should be edited: just the one indicated in `message_id`, messages in the same topic that had been sent after this one, or all of them.  Only the default value of `change_one` is valid when editing only the content of a message.  This parameter determines both which messages get moved and also whether clients that are currently narrowed to the topic containing the message should navigate or adjust their compose box recipient to point to the post-edit stream/topic. 
my $send_notification_to_old_thread = true; # boolean | Whether to send breadcrumb message to the old thread to notify users where the messages were moved to.  **Changes**: New in Zulip 3.0 (feature level 9). 
my $send_notification_to_new_thread = true; # boolean | Whether to send a notification message to the new thread to notify users where the messages came from.  **Changes**: New in Zulip 3.0 (feature level 9). 
my $content = Hello; # string | The content of the message. Maximum message size of 10000 bytes. 
my $stream_id = 42; # int | The stream ID to move the message(s) to, to request moving messages to another stream.  Should only be sent when changing the stream, and will throw an error if the target message is not a stream message. 

eval { 
    my $result = $api_instance->update_message(message_id => $message_id, topic => $topic, propagate_mode => $propagate_mode, send_notification_to_old_thread => $send_notification_to_old_thread, send_notification_to_new_thread => $send_notification_to_new_thread, content => $content, stream_id => $stream_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->update_message: $@\n";
}
```

