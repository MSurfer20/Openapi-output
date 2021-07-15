### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $include_public = false; # boolean | Include all public streams. 
my $include_web_public = true; # boolean | Include all web public streams. 
my $include_subscribed = false; # boolean | Include all streams that the user is subscribed to. 
my $include_all_active = true; # boolean | Include all active streams. The user must have administrative privileges to use this parameter. 
my $include_default = true; # boolean | Include all default streams for the user's realm. 
my $include_owner_subscribed = true; # boolean | If the user is a bot, include all streams that the bot's owner is subscribed to. 

eval { 
    my $result = $api_instance->get_streams(include_public => $include_public, include_web_public => $include_web_public, include_subscribed => $include_subscribed, include_all_active => $include_all_active, include_default => $include_default, include_owner_subscribed => $include_owner_subscribed);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->get_streams: $@\n";
}
```

