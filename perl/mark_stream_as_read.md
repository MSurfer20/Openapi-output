### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $stream_id = 42; # int | The ID of the stream to access. 

eval { 
    my $result = $api_instance->mark_stream_as_read(stream_id => $stream_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->mark_stream_as_read: $@\n";
}
```

