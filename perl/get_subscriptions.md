### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $include_subscribers = true; # boolean | Whether each returned stream object should include a `subscribers` field containing a list of the user IDs of its subscribers.  (This may be significantly slower in organizations with thousands of users subscribed to many streams.)  **Changes**: New in Zulip 2.1.0. 

eval { 
    my $result = $api_instance->get_subscriptions(include_subscribers => $include_subscribers);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->get_subscriptions: $@\n";
}
```

