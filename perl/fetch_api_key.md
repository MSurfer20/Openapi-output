### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::AuthenticationApi;
my $api_instance = WWW::OpenAPIClient::AuthenticationApi->new(
);

my $username = iago@zulip.com; # string | The username to be used for authentication (typically, the email address, but depending on configuration, it could be an LDAP username).  See the `require_email_format_usernames` parameter documented in [GET /server_settings](/api/get-server-settings) for details. 
my $password = abcd1234; # string | The user's Zulip password (or LDAP password, if LDAP authentication is in use). 

eval { 
    my $result = $api_instance->fetch_api_key(username => $username, password => $password);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AuthenticationApi->fetch_api_key: $@\n";
}
```

