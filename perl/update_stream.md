### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $stream_id = 1; # int | The ID of the stream to access. 
my $description = Discuss Italian history and travel destinations.; # string | The new description for the stream. Limited Zulip markdown is allowed in this field.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64). 
my $new_name = Italy; # string | The new name for the stream.  **Changes**: Removed unnecessary JSON-encoding of this parameter in Zulip 4.0 (feature level 64). 
my $is_private = true; # boolean | Change whether the stream is a private stream. 
my $is_announcement_only = true; # boolean | Whether the stream is limited to announcements.  **Changes**: Deprecated in Zulip 3.0 (feature level 1), use   `stream_post_policy` instead. 
my $stream_post_policy = 2; # int | Policy for which users can post messages to the stream.  * 1 => Any user can post. * 2 => Only administrators can post. * 3 => Only full members can post. * 4 => Only moderators can post.  **Changes**: New in Zulip 3.0, replacing the previous `is_announcement_only` boolean. 
my $history_public_to_subscribers = false; # boolean | Whether the stream's message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream.  Corresponds to the [shared history](/help/stream-permissions) option in documentation. 
my $message_retention_days = 20; # OneOfstringinteger | Number of days that messages sent to this stream will be stored before being automatically deleted by the [message retention policy](/help/message-retention-policy).  Two special string format values are supported:  * \"realm_default\" => Return to the organization-level setting. * \"forever\" => Retain messages forever.  **Changes**: New in Zulip 3.0 (feature level 17). 

eval { 
    my $result = $api_instance->update_stream(stream_id => $stream_id, description => $description, new_name => $new_name, is_private => $is_private, is_announcement_only => $is_announcement_only, stream_post_policy => $stream_post_policy, history_public_to_subscribers => $history_public_to_subscribers, message_retention_days => $message_retention_days);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->update_stream: $@\n";
}
```

