### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);

my $filter_id = 42; # int | The ID of the linkifier that you want to remove. 

eval { 
    my $result = $api_instance->remove_linkifier(filter_id => $filter_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->remove_linkifier: $@\n";
}
```

