# ImageBuildBinding

ImageBuildBinding specifies binding configuration for the build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of binding. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_binding import ImageBuildBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildBinding from a JSON string
image_build_binding_instance = ImageBuildBinding.from_json(json)
# print the JSON string representation of the object
print(ImageBuildBinding.to_json())

# convert the object into a dict
image_build_binding_dict = image_build_binding_instance.to_dict()
# create an instance of ImageBuildBinding from a dict
image_build_binding_from_dict = ImageBuildBinding.from_dict(image_build_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


