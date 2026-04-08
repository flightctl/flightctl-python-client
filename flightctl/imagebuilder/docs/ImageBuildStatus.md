# ImageBuildStatus

ImageBuildStatus represents the current status of an ImageBuild.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[ImageBuildCondition]**](ImageBuildCondition.md) | Current conditions of the ImageBuild. | [optional] 
**image_reference** | **str** | The full image reference of the built image (e.g., quay.io/org/imagename:tag). | [optional] 
**architecture** | **str** | The architecture of the built image. | [optional] 
**manifest_digest** | **str** | The digest of the built image manifest. | [optional] 
**last_seen** | **datetime** | The last time the build was seen (heartbeat). | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_build_status import ImageBuildStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildStatus from a JSON string
image_build_status_instance = ImageBuildStatus.from_json(json)
# print the JSON string representation of the object
print(ImageBuildStatus.to_json())

# convert the object into a dict
image_build_status_dict = image_build_status_instance.to_dict()
# create an instance of ImageBuildStatus from a dict
image_build_status_from_dict = ImageBuildStatus.from_dict(image_build_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


