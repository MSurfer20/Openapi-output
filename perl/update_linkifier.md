### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);

my $filter_id = 2; # int | The ID of the linkifier that you want to update. 
my $pattern = #(?P<id>[0-9]+); # string | The [Python regular expression](https://docs.python.org/3/howto/regex.html) that should trigger the linkifier. 
my $url_format_string = https://github.com/zulip/zulip/issues/%(id)s; # string | The URL used for the link. If you used named groups for the `pattern`, you can insert their content here with `%(name_of_the_capturing_group)s`. 

eval { 
    my $result = $api_instance->update_linkifier(filter_id => $filter_id, pattern => $pattern, url_format_string => $url_format_string);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->update_linkifier: $@\n";
}
```

