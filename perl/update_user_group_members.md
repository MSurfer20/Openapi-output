### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_group_id = 1; # int | The ID of the target user group. 
my $delete = [(null)]; # ARRAY[int] | The list of user ids to be removed from the user group. 
my $add = [(null)]; # ARRAY[int] | The list of user ids to be added to the user group. 

eval { 
    my $result = $api_instance->update_user_group_members(user_group_id => $user_group_id, delete => $delete, add => $add);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->update_user_group_members: $@\n";
}
```

