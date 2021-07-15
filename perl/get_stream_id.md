### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $stream = Denmark; # string | The name of the stream to access. 

eval { 
    my $result = $api_instance->get_stream_id(stream => $stream);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->get_stream_id: $@\n";
}
```

