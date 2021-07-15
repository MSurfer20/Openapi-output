### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $user_id = 12; # int | The target user's ID. 
my $client_gravatar = true; # boolean | Whether the client supports computing gravatars URLs.  If enabled, `avatar_url` will be included in the response only if there is a Zulip avatar, and will be `null` for users who are using gravatar as their avatar.  This option significantly reduces the compressed size of user data, since gravatar URLs are long, random strings and thus do not compress well. The `client_gravatar` field is set to `true` if clients can compute their own gravatars. 
my $include_custom_profile_fields = true; # boolean | Whether the client wants [custom profile field](/help/add-custom-profile-fields) data to be included in the response.  **Changes**: New in Zulip 2.1.0.  Previous versions do no offer these data via the API. 

eval { 
    my $result = $api_instance->get_user(user_id => $user_id, client_gravatar => $client_gravatar, include_custom_profile_fields => $include_custom_profile_fields);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->get_user: $@\n";
}
```

