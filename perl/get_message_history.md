### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $message_id = 42; # int | The target message's ID. 

eval { 
    my $result = $api_instance->get_message_history(message_id => $message_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->get_message_history: $@\n";
}
```

