### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);


eval { 
    my $result = $api_instance->create_big_blue_button_video_call();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->create_big_blue_button_video_call: $@\n";
}
```

