### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::RealTimeEventsApi;
my $api_instance = WWW::OpenAPIClient::RealTimeEventsApi->new(
);


eval { 
    $api_instance->rest_error_handling();
};
if ($@) {
    warn "Exception when calling RealTimeEventsApi->rest_error_handling: $@\n";
}
```

