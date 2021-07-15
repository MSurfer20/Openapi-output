### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_id = 12; # int | The target user's ID. 
my $full_name = "full_name_example"; # string | The user's full name. 
my $role = 400; # int | New [role](/help/roles-and-permissions) for the user.  Roles are encoded as:  * Organization owner: 100 * Organization administrator: 200 * Organization moderator: 300 * Member: 400 * Guest: 600  Only organization owners can add or remove the owner role.  The owner role cannot be removed from the only organization owner.  **Changes**: New in Zulip 3.0 (feature level 8), replacing the previous pair of `is_admin` and `is_guest` boolean parameters. Organization moderator role added in Zulip 4.0 (feature level 60). 
my $profile_data = [(null)]; # ARRAY[object] | A dictionary containing the to be updated custom profile field data for the user. 

eval { 
    my $result = $api_instance->update_user(user_id => $user_id, full_name => $full_name, role => $role, profile_data => $profile_data);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->update_user: $@\n";
}
```

