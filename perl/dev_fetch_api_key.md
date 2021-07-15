### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::AuthenticationApi;
my $api_instance = WWW::OpenAPIClient::AuthenticationApi->new(
);

my $username = iago@zulip.com; # string | The email address for the user that owns the API key. 

eval { 
    my $result = $api_instance->dev_fetch_api_key(username => $username);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AuthenticationApi->dev_fetch_api_key: $@\n";
}
```

