### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);


eval { 
    my $result = $api_instance->get_user_groups();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->get_user_groups: $@\n";
}
```

