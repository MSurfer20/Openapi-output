### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $subscriptions = [("null")]; # ARRAY[string] | A list of stream names to unsubscribe from. This parameter is called `streams` in our Python API. 
my $principals = [(new WWW::OpenAPIClient.OneOfstringinteger())]; # ARRAY[OneOfstringinteger] | A list of user ids (preferred) or Zulip display email addresses of the users to be subscribed to or unsubscribed from the streams specified in the `subscriptions` parameter. If not provided, then the requesting user/bot is subscribed.  **Changes**: The integer format is new in Zulip 3.0 (feature level 9). 

eval { 
    my $result = $api_instance->unsubscribe(subscriptions => $subscriptions, principals => $principals);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->unsubscribe: $@\n";
}
```

