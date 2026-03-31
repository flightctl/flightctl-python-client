# ImageBuildUserConfiguration

ImageBuildUserConfiguration specifies user configuration for the build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for the user configuration. | 
**publickey** | **str** | The public key for the user configuration. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_user_configuration import ImageBuildUserConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildUserConfiguration from a JSON string
image_build_user_configuration_instance = ImageBuildUserConfiguration.from_json(json)
# print the JSON string representation of the object
print(ImageBuildUserConfiguration.to_json())

# convert the object into a dict
image_build_user_configuration_dict = image_build_user_configuration_instance.to_dict()
# create an instance of ImageBuildUserConfiguration from a dict
image_build_user_configuration_from_dict = ImageBuildUserConfiguration.from_dict(image_build_user_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


