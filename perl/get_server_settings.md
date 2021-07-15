### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);


eval { 
    my $result = $api_instance->get_server_settings();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->get_server_settings: $@\n";
}
```

