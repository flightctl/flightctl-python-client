# ImageMountVolumeProviderSpec

Volume from OCI image mounted at specified path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ImageVolumeSource**](ImageVolumeSource.md) |  | 
**mount** | [**VolumeMount**](VolumeMount.md) |  | 

## Example

```python
from flightctl.models.image_mount_volume_provider_spec import ImageMountVolumeProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMountVolumeProviderSpec from a JSON string
image_mount_volume_provider_spec_instance = ImageMountVolumeProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ImageMountVolumeProviderSpec.to_json())

# convert the object into a dict
image_mount_volume_provider_spec_dict = image_mount_volume_provider_spec_instance.to_dict()
# create an instance of ImageMountVolumeProviderSpec from a dict
image_mount_volume_provider_spec_from_dict = ImageMountVolumeProviderSpec.from_dict(image_mount_volume_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


