### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $subscriptions = [(null)]; # ARRAY[object] | A list of dictionaries containing the key `name` and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created. The description of the stream created can be specified by setting the dictionary key `description` with an appropriate value. 
my $principals = [(new WWW::OpenAPIClient.OneOfstringinteger())]; # ARRAY[OneOfstringinteger] | A list of user ids (preferred) or Zulip display email addresses of the users to be subscribed to or unsubscribed from the streams specified in the `subscriptions` parameter. If not provided, then the requesting user/bot is subscribed.  **Changes**: The integer format is new in Zulip 3.0 (feature level 9). 
my $authorization_errors_fatal = false; # boolean | A boolean specifying whether authorization errors (such as when the requesting user is not authorized to access a private stream) should be considered fatal or not. When `True`, an authorization error is reported as such. When set to `False`, the response will be a 200 and any streams where the request encountered an authorization error will be listed in the `unauthorized` key. 
my $announce = true; # boolean | If one of the streams specified did not exist previously and is thus craeted by this call, this determines whether [notification bot](/help/configure-notification-bot) will send an announcement about the new stream's creation. 
my $invite_only = true; # boolean | As described above, this endpoint will create a new stream if passed a stream name that doesn't already exist.  This parameters and the ones that follow are used to request an initial configuration of a created stream; they are ignored for streams that already exist.  This parameter determines whether any newly created streams will be private streams. 
my $history_public_to_subscribers = false; # boolean | Whether the stream's message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream.  Corresponds to the [shared history](/help/stream-permissions) option in documentation. 
my $stream_post_policy = 2; # int | Policy for which users can post messages to the stream.  * 1 => Any user can post. * 2 => Only administrators can post. * 3 => Only full members can post. * 4 => Only moderators can post.  **Changes**: New in Zulip 3.0, replacing the previous `is_announcement_only` boolean. 
my $message_retention_days = 20; # OneOfstringinteger | Number of days that messages sent to this stream will be stored before being automatically deleted by the [message retention policy](/help/message-retention-policy).  Two special string format values are supported:  * \"realm_default\" => Return to the organization-level setting. * \"forever\" => Retain messages forever.  **Changes**: New in Zulip 3.0 (feature level 17). 

eval { 
    my $result = $api_instance->subscribe(subscriptions => $subscriptions, principals => $principals, authorization_errors_fatal => $authorization_errors_fatal, announce => $announce, invite_only => $invite_only, history_public_to_subscribers => $history_public_to_subscribers, stream_post_policy => $stream_post_policy, message_retention_days => $message_retention_days);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->subscribe: $@\n";
}
```

