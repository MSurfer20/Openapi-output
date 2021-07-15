### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::RealTimeEventsApi;
my $api_instance = WWW::OpenAPIClient::RealTimeEventsApi->new(
);

my $event_types = [("null")]; # ARRAY[string] | A JSON-encoded array indicating which types of events you're interested in. Values that you might find useful include:    * **message** (messages)   * **subscription** (changes in your subscriptions)   * **realm_user** (changes to users in the organization and     their properties, such as their name).  If you do not specify this parameter, you will receive all events, and have to filter out the events not relevant to your client in your client code.  For most applications, one is only interested in messages, so one specifies: `event_types=['message']`  Event types not supported by the server are ignored, in order to simplify the implementation of client apps that support multiple server versions. 
my $narrow = [(null)]; # ARRAY[ARRAY[string]] | A JSON-encoded array of arrays of length 2 indicating the narrow for which you'd like to receive events for. For instance, to receive events for the stream `Denmark`, you would specify `narrow=[['stream', 'Denmark']]`.  Another example is `narrow=[['is', 'private']]` for private messages. Default is `[]`. 
my $all_public_streams = true; # boolean | Whether you would like to request message events from all public streams.  Useful for workflow bots that you'd like to see all new messages sent to public streams.  (You can also subscribe the user to private streams). 

eval { 
    $api_instance->real_time_post(event_types => $event_types, narrow => $narrow, all_public_streams => $all_public_streams);
};
if ($@) {
    warn "Exception when calling RealTimeEventsApi->real_time_post: $@\n";
}
```

