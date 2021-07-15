### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);


eval { 
    my $result = $api_instance->deactivate_own_user();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->deactivate_own_user: $@\n";
}
```

