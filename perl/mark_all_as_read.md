### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);


eval { 
    my $result = $api_instance->mark_all_as_read();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->mark_all_as_read: $@\n";
}
```

