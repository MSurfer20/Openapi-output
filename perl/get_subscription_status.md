### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $user_id = 12; # int | The target user's ID. 
my $stream_id = 1; # int | The ID of the stream to access. 

eval { 
    my $result = $api_instance->get_subscription_status(user_id => $user_id, stream_id => $stream_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->get_subscription_status: $@\n";
}
```

