### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $filename = "/path/to/file"; # string | 

eval { 
    my $result = $api_instance->upload_file(filename => $filename);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->upload_file: $@\n";
}
```

