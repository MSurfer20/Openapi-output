### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $message_id = 42; # int | The target message's ID. 

eval { 
    my $result = $api_instance->delete_message(message_id => $message_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->delete_message: $@\n";
}
```

