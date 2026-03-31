# ImageBuildList

ImageBuildList is a list of ImageBuild resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[ImageBuild]**](ImageBuild.md) | List of ImageBuild resources. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_list import ImageBuildList

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildList from a JSON string
image_build_list_instance = ImageBuildList.from_json(json)
# print the JSON string representation of the object
print(ImageBuildList.to_json())

# convert the object into a dict
image_build_list_dict = image_build_list_instance.to_dict()
# create an instance of ImageBuildList from a dict
image_build_list_from_dict = ImageBuildList.from_dict(image_build_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


