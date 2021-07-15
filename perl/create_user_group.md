### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $name = marketing; # string | The name of the user group. 
my $description = The marketing team.; # string | The description of the user group. 
my $members = [(null)]; # ARRAY[int] | An array containing the user IDs of the initial members for the new user group. 

eval { 
    my $result = $api_instance->create_user_group(name => $name, description => $description, members => $members);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->create_user_group: $@\n";
}
```

