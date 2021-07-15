### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::WebhooksApi;
my $api_instance = WWW::OpenAPIClient::WebhooksApi->new(
);


eval { 
    my $result = $api_instance->zulip_outgoing_webhooks();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling WebhooksApi->zulip_outgoing_webhooks: $@\n";
}
```

