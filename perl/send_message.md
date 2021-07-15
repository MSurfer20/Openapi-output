### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $type = private; # string | The type of message to be sent. `private` for a private message and `stream` for a stream message. 
my $to = [(null)]; # ARRAY[int] | For stream messages, either the name or integer ID of the stream. For private messages, either a list containing integer user IDs or a list containing string email addresses.  **Changes**: Support for using user/stream IDs was added in Zulip 2.0.0. 
my $content = Hello; # string | The content of the message. Maximum message size of 10000 bytes. 
my $topic = Castle; # string | The topic of the message. Only required for stream messages (`type=\"stream\"`), ignored otherwise.  Maximum length of 60 characters.  **Changes**: New in Zulip 2.0.  Previous Zulip releases encoded this as `subject`, which is currently a deprecated alias. 
my $queue_id = 1593114627:0; # string | For clients supporting [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo), the [event queue](/api/register-queue) ID for the client.  If passed, `local_id` is required.  If the message is successfully sent, the server will include `local_id` in the `message` event that the client with this `queue_id` will receive notifying it of the new message via [`GET /events`](/api/get-events).  This lets the client know unambiguously that it should replace the locally echoed message, rather than adding this new message (which would be correct if the user had sent the new message from another device). 
my $local_id = 100.01; # string | For clients supporting local echo, a unique string-format identifier chosen freely by the client; the server will pass it back to the client without inspecting it, as described in the `queue_id` description. 

eval { 
    my $result = $api_instance->send_message(type => $type, to => $to, content => $content, topic => $topic, queue_id => $queue_id, local_id => $local_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->send_message: $@\n";
}
```

