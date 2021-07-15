### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::RealTimeEventsApi;
my $api_instance = WWW::OpenAPIClient::RealTimeEventsApi->new(
);

my $queue_id = 1375801870:2942; # string | The ID of an event queue that was previously registered via `POST /api/v1/register` (see [Register a queue](/api/register-queue)). 
my $last_event_id = -1; # int | The highest event ID in this queue that you've received and wish to acknowledge. See the [code for `call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/master/zulip/zulip/__init__.py) in the [zulip Python module](https://github.com/zulip/python-zulip-api) for an example implementation of correctly processing each event exactly once. 
my $dont_block = true; # boolean | Set to `true` if the client is requesting a nonblocking reply. If not specified, the request will block until either a new event is available or a few minutes have passed, in which case the server will send the client a heartbeat event. 

eval { 
    my $result = $api_instance->get_events(queue_id => $queue_id, last_event_id => $last_event_id, dont_block => $dont_block);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling RealTimeEventsApi->get_events: $@\n";
}
```

