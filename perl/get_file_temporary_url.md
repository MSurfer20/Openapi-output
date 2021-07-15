### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $realm_id_str = 1; # int | The realm id. 
my $filename = 4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt; # string | Path to the URL. 

eval { 
    my $result = $api_instance->get_file_temporary_url(realm_id_str => $realm_id_str, filename => $filename);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->get_file_temporary_url: $@\n";
}
```

