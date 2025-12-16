# MountVolumeProviderSpec

Named volume mount configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount** | [**VolumeMount**](VolumeMount.md) |  | 

## Example

```python
from flightctl.models.mount_volume_provider_spec import MountVolumeProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of MountVolumeProviderSpec from a JSON string
mount_volume_provider_spec_instance = MountVolumeProviderSpec.from_json(json)
# print the JSON string representation of the object
print(MountVolumeProviderSpec.to_json())

# convert the object into a dict
mount_volume_provider_spec_dict = mount_volume_provider_spec_instance.to_dict()
# create an instance of MountVolumeProviderSpec from a dict
mount_volume_provider_spec_from_dict = MountVolumeProviderSpec.from_dict(mount_volume_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


