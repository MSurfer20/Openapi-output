### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_id = 12; # int | The target user's ID. 

eval { 
    my $result = $api_instance->reactivate_user(user_id => $user_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->reactivate_user: $@\n";
}
```

