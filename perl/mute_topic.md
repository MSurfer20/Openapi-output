### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $topic = dinner; # string | The topic to (un)mute. Note that the request will succeed regardless of whether any messages have been sent to the specified topic. 
my $op = add; # string | Whether to mute (`add`) or unmute (`remove`) the provided topic. 
my $stream = Denmark; # string | The name of the stream to access. 
my $stream_id = 42; # int | The ID of the stream to access. 

eval { 
    my $result = $api_instance->mute_topic(topic => $topic, op => $op, stream => $stream, stream_id => $stream_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->mute_topic: $@\n";
}
```

