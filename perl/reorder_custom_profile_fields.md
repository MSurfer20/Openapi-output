### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);

my $order = [(null)]; # ARRAY[int] | A list of the IDs of all the custom profile fields defined in this organization, in the desired new order. 

eval { 
    my $result = $api_instance->reorder_custom_profile_fields(order => $order);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->reorder_custom_profile_fields: $@\n";
}
```

