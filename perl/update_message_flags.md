### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $messages = [(null)]; # ARRAY[int] | An array containing the IDs of the target messages. 
my $op = add; # string | Whether to `add` the flag or `remove` it. 
my $flag = read; # string | The flag that should be added/removed. 

eval { 
    my $result = $api_instance->update_message_flags(messages => $messages, op => $op, flag => $flag);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->update_message_flags: $@\n";
}
```

