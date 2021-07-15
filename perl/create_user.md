### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $email = username@example.com; # string | The email address of the new user. 
my $password = abcd1234; # string | The password of the new user. 
my $full_name = New User; # string | The full name of the new user. 

eval { 
    my $result = $api_instance->create_user(email => $email, password => $password, full_name => $full_name);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->create_user: $@\n";
}
```

