### Example

```python
import time
import openapi_client
from openapi_client.api import server_and_organizations_api
from openapi_client.model.str_bool_date_datetime_dict_float_int_list_str_none_type import StrBoolDateDatetimeDictFloatIntListStrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://example.zulipchat.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.zulipchat.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = server_and_organizations_api.ServerAndOrganizationsApi(api_client)
    field_type = 3 # int | The field type can be any of the supported custom profile field types. See the [custom profile fields documentation](/help/add-custom-profile-fields) more details on what each type means.  * **1**: Short text * **2**: Long text * **3**: List of options * **4**: Date picker * **5**: Link * **6**: Person picker * **7**: External account 
    name = "Favorite programming language" # str | The name of the custom profile field, which will appear both in user-facing settings UI for configuring custom profile fields and in UI displaying a user's profile.  (optional)
    hint = "Your favorite programming language." # str | The help text to be displayed for the custom profile field in user-facing settings UI for configuring custom profile fields.  (optional)
    field_data =  # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Field types 3 (List of options) and 7 (External account) support storing additional configuration for the field type in the `field_data` attribute.  For field type 3 (List of options), this attribute is a JSON dictionary defining the choices and the order they will be displayed in the dropdown UI for individual users to select an option.  The interface for field type 7 is not yet stabilized.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a custom profile field
        api_response = api_instance.create_custom_profile_field(field_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerAndOrganizationsApi->create_custom_profile_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a custom profile field
        api_response = api_instance.create_custom_profile_field(field_type, name=name, hint=hint, field_data=field_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerAndOrganizationsApi->create_custom_profile_field: %s\n" % e)
```


