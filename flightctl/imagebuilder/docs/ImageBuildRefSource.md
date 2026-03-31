# ImageBuildRefSource

ImageBuildRefSource specifies a source image from an ImageBuild resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of source. | 
**image_build_ref** | **str** | The name of the ImageBuild resource to use as source. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_ref_source import ImageBuildRefSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildRefSource from a JSON string
image_build_ref_source_instance = ImageBuildRefSource.from_json(json)
# print the JSON string representation of the object
print(ImageBuildRefSource.to_json())

# convert the object into a dict
image_build_ref_source_dict = image_build_ref_source_instance.to_dict()
# create an instance of ImageBuildRefSource from a dict
image_build_ref_source_from_dict = ImageBuildRefSource.from_dict(image_build_ref_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


