# ImageBuildSource

ImageBuildSource specifies the source image for the build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The name of the Repository resource of type OCI containing the source image. | 
**image_name** | **str** | The name of the source image. | 
**image_tag** | **str** | The tag of the source image. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_source import ImageBuildSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildSource from a JSON string
image_build_source_instance = ImageBuildSource.from_json(json)
# print the JSON string representation of the object
print(ImageBuildSource.to_json())

# convert the object into a dict
image_build_source_dict = image_build_source_instance.to_dict()
# create an instance of ImageBuildSource from a dict
image_build_source_from_dict = ImageBuildSource.from_dict(image_build_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


