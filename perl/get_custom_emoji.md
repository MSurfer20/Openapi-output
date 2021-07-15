### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);


eval { 
    my $result = $api_instance->get_custom_emoji();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->get_custom_emoji: $@\n";
}
```

