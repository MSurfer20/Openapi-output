### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $msg_ids = [(null)]; # ARRAY[int] | List of IDs for the messages to check.
my $narrow = [(null)]; # ARRAY[object] | A structure defining the narrow to check against. See how to [construct a narrow](/api/construct-narrow).

eval { 
    my $result = $api_instance->check_messages_match_narrow(msg_ids => $msg_ids, narrow => $narrow);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->check_messages_match_narrow: $@\n";
}
```

