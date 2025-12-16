# VolumeMount

Mount configuration for a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Mount path in the container with support for options. | 

## Example

```python
from flightctl.models.volume_mount import VolumeMount

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeMount from a JSON string
volume_mount_instance = VolumeMount.from_json(json)
# print the JSON string representation of the object
print(VolumeMount.to_json())

# convert the object into a dict
volume_mount_dict = volume_mount_instance.to_dict()
# create an instance of VolumeMount from a dict
volume_mount_from_dict = VolumeMount.from_dict(volume_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


