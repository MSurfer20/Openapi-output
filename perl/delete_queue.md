### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::RealTimeEventsApi;
my $api_instance = WWW::OpenAPIClient::RealTimeEventsApi->new(
);

my $queue_id = 1375801870:2942; # string | The ID of an event queue that was previously registered via `POST /api/v1/register` (see [Register a queue](/api/register-queue)). 

eval { 
    my $result = $api_instance->delete_queue(queue_id => $queue_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling RealTimeEventsApi->delete_queue: $@\n";
}
```

