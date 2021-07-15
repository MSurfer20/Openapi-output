### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_group_id = 1; # int | The ID of the target user group. 
my $name = marketing team; # string | The new name of the group. 
my $description = The marketing team.; # string | The new description of the group. 

eval { 
    my $result = $api_instance->update_user_group(user_group_id => $user_group_id, name => $name, description => $description);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->update_user_group: $@\n";
}
```

