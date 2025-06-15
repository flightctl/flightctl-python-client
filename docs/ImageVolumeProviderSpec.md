# ImageVolumeProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ImageVolumeSource**](ImageVolumeSource.md) |  | 

## Example

```python
from flightctl.models.image_volume_provider_spec import ImageVolumeProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageVolumeProviderSpec from a JSON string
image_volume_provider_spec_instance = ImageVolumeProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ImageVolumeProviderSpec.to_json())

# convert the object into a dict
image_volume_provider_spec_dict = image_volume_provider_spec_instance.to_dict()
# create an instance of ImageVolumeProviderSpec from a dict
image_volume_provider_spec_from_dict = ImageVolumeProviderSpec.from_dict(image_volume_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


