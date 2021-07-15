### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::UsersApi;
my $api_instance = WWW::OpenAPIClient::UsersApi->new(
);

my $op = start; # string | Whether the user has started (`start`) or stopped (`stop`) to type. 
my $to = [(null)]; # ARRAY[int] | For 'private' type it is the user_ids of the recipients of the message being typed. Send a JSON-encoded list of user_ids. (Use a list even if there is only one recipient.)  For 'stream' type it is a single element list containing ID of stream in which the message is being typed.  **Changes**: Before Zulip 2.0, this parameter accepted only a JSON-encoded list of email addresses.  Support for the email address-based format was removed in Zulip 3.0 (feature level 11). 
my $type = private; # string | Type of the message being composed. 
my $topic = typing notifications; # string | Topic to which message is being typed. Required for the 'stream' type. Ignored in case of 'private' type. 

eval { 
    my $result = $api_instance->set_typing_status(op => $op, to => $to, type => $type, topic => $topic);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling UsersApi->set_typing_status: $@\n";
}
```

