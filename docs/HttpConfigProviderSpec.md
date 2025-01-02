# HttpConfigProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the config provider. | 
**http_ref** | [**HttpConfigProviderSpecHttpRef**](HttpConfigProviderSpecHttpRef.md) |  | 

## Example

```python
from flightctl.models.http_config_provider_spec import HttpConfigProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConfigProviderSpec from a JSON string
http_config_provider_spec_instance = HttpConfigProviderSpec.from_json(json)
# print the JSON string representation of the object
print(HttpConfigProviderSpec.to_json())

# convert the object into a dict
http_config_provider_spec_dict = http_config_provider_spec_instance.to_dict()
# create an instance of HttpConfigProviderSpec from a dict
http_config_provider_spec_from_dict = HttpConfigProviderSpec.from_dict(http_config_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


