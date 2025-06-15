# ApplicationVolumeProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 

## Example

```python
from flightctl.models.application_volume_provider_spec import ApplicationVolumeProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVolumeProviderSpec from a JSON string
application_volume_provider_spec_instance = ApplicationVolumeProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ApplicationVolumeProviderSpec.to_json())

# convert the object into a dict
application_volume_provider_spec_dict = application_volume_provider_spec_instance.to_dict()
# create an instance of ApplicationVolumeProviderSpec from a dict
application_volume_provider_spec_from_dict = ApplicationVolumeProviderSpec.from_dict(application_volume_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


