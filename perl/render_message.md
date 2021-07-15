### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $content = Hello; # string | The content of the message. Maximum message size of 10000 bytes. 

eval { 
    my $result = $api_instance->render_message(content => $content);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->render_message: $@\n";
}
```

