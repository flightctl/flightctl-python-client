# ImageBuild

ImageBuild represents a build request for a container image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**ImageBuildSpec**](ImageBuildSpec.md) |  | 
**status** | [**ImageBuildStatus**](ImageBuildStatus.md) |  | [optional] 
**imageexports** | [**List[ImageExport]**](ImageExport.md) | Array of ImageExport resources that reference this ImageBuild. Only populated when withExports query parameter is true. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_build import ImageBuild

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuild from a JSON string
image_build_instance = ImageBuild.from_json(json)
# print the JSON string representation of the object
print(ImageBuild.to_json())

# convert the object into a dict
image_build_dict = image_build_instance.to_dict()
# create an instance of ImageBuild from a dict
image_build_from_dict = ImageBuild.from_dict(image_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


