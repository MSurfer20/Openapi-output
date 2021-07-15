### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);

my $playground_id = 1; # int | The ID of the playground that you want to remove. 

eval { 
    my $result = $api_instance->remove_code_playground(playground_id => $playground_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->remove_code_playground: $@\n";
}
```

