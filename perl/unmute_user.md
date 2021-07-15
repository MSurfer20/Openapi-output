### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $muted_user_id = 10; # int | The ID of the user to mute/un-mute. 

eval { 
    my $result = $api_instance->unmute_user(muted_user_id => $muted_user_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->unmute_user: $@\n";
}
```

