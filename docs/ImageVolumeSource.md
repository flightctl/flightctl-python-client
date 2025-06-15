# ImageVolumeSource

Describes the source of an OCI-compliant image or artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Reference to an OCI-compliant image or artifact in a registry. This may be a container image or another type of OCI artifact, as long as it conforms to the OCI image specification. | 

## Example

```python
from flightctl.models.image_volume_source import ImageVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImageVolumeSource from a JSON string
image_volume_source_instance = ImageVolumeSource.from_json(json)
# print the JSON string representation of the object
print(ImageVolumeSource.to_json())

# convert the object into a dict
image_volume_source_dict = image_volume_source_instance.to_dict()
# create an instance of ImageVolumeSource from a dict
image_volume_source_from_dict = ImageVolumeSource.from_dict(image_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


