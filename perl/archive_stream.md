### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $stream_id = 1; # int | The ID of the stream to access. 

eval { 
    my $result = $api_instance->archive_stream(stream_id => $stream_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->archive_stream: $@\n";
}
```

