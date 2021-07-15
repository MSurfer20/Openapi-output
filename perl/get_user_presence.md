### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_id_or_email = iago@zulip.com; # string | The user_id or Zulip display email address of the user whose presence you want to fetch.  **Changes**: New in Zulip 4.0 (feature level 43). Previous versions only supported identifying the user by Zulip display email. 

eval { 
    my $result = $api_instance->get_user_presence(user_id_or_email => $user_id_or_email);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->get_user_presence: $@\n";
}
```

