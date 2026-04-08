# ImageBuildSpec

ImageBuildSpec describes the specification for an image build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ImageBuildSource**](ImageBuildSource.md) |  | 
**destination** | [**ImageBuildDestination**](ImageBuildDestination.md) |  | 
**binding** | [**ImageBuildBinding**](ImageBuildBinding.md) |  | 
**user_configuration** | [**ImageBuildUserConfiguration**](ImageBuildUserConfiguration.md) |  | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_build_spec import ImageBuildSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildSpec from a JSON string
image_build_spec_instance = ImageBuildSpec.from_json(json)
# print the JSON string representation of the object
print(ImageBuildSpec.to_json())

# convert the object into a dict
image_build_spec_dict = image_build_spec_instance.to_dict()
# create an instance of ImageBuildSpec from a dict
image_build_spec_from_dict = ImageBuildSpec.from_dict(image_build_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


