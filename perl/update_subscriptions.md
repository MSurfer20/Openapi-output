### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $delete = [("null")]; # ARRAY[string] | A list of stream names to unsubscribe from. 
my $add = [(null)]; # ARRAY[object] | A list of objects describing which streams to subscribe to, optionally including per-user subscription parameters (e.g. color) and if the stream is to be created, its description. 

eval { 
    my $result = $api_instance->update_subscriptions(delete => $delete, add => $add);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->update_subscriptions: $@\n";
}
```

