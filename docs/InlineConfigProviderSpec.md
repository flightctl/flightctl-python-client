# InlineConfigProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the config provider. | 
**inline** | [**List[FileSpec]**](FileSpec.md) | A list of files to create on the device. | 

## Example

```python
from flightctl.models.inline_config_provider_spec import InlineConfigProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of InlineConfigProviderSpec from a JSON string
inline_config_provider_spec_instance = InlineConfigProviderSpec.from_json(json)
# print the JSON string representation of the object
print(InlineConfigProviderSpec.to_json())

# convert the object into a dict
inline_config_provider_spec_dict = inline_config_provider_spec_instance.to_dict()
# create an instance of InlineConfigProviderSpec from a dict
inline_config_provider_spec_from_dict = InlineConfigProviderSpec.from_dict(inline_config_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


