# InlineApplicationProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 

## Example

```python
from flightctl.models.inline_application_provider_spec import InlineApplicationProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of InlineApplicationProviderSpec from a JSON string
inline_application_provider_spec_instance = InlineApplicationProviderSpec.from_json(json)
# print the JSON string representation of the object
print(InlineApplicationProviderSpec.to_json())

# convert the object into a dict
inline_application_provider_spec_dict = inline_application_provider_spec_instance.to_dict()
# create an instance of InlineApplicationProviderSpec from a dict
inline_application_provider_spec_from_dict = InlineApplicationProviderSpec.from_dict(inline_application_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


