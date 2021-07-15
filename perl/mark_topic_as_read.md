### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $stream_id = 42; # int | The ID of the stream to access. 
my $topic_name = new coffee machine; # string | The name of the topic whose messages should be marked as read. 

eval { 
    my $result = $api_instance->mark_topic_as_read(stream_id => $stream_id, topic_name => $topic_name);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->mark_topic_as_read: $@\n";
}
```

