### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::ServerAndOrganizationsApi;
my $api_instance = WWW::OpenAPIClient::ServerAndOrganizationsApi->new(
);

my $field_type = 3; # int | The field type can be any of the supported custom profile field types. See the [custom profile fields documentation](/help/add-custom-profile-fields) more details on what each type means.  * **1**: Short text * **2**: Long text * **3**: List of options * **4**: Date picker * **5**: Link * **6**: Person picker * **7**: External account 
my $name = Favorite programming language; # string | The name of the custom profile field, which will appear both in user-facing settings UI for configuring custom profile fields and in UI displaying a user's profile. 
my $hint = Your favorite programming language.; # string | The help text to be displayed for the custom profile field in user-facing settings UI for configuring custom profile fields. 
my $field_data = null; # object | Field types 3 (List of options) and 7 (External account) support storing additional configuration for the field type in the `field_data` attribute.  For field type 3 (List of options), this attribute is a JSON dictionary defining the choices and the order they will be displayed in the dropdown UI for individual users to select an option.  The interface for field type 7 is not yet stabilized. 

eval { 
    my $result = $api_instance->create_custom_profile_field(field_type => $field_type, name => $name, hint => $hint, field_data => $field_data);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ServerAndOrganizationsApi->create_custom_profile_field: $@\n";
}
```

