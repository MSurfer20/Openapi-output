### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_group_id = 1; # int | The ID of the target user group. 

eval { 
    my $result = $api_instance->remove_user_group(user_group_id => $user_group_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->remove_user_group: $@\n";
}
```

