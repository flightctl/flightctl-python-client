# ImageExport

ImageExport represents an export request to convert and push images to different formats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**ImageExportSpec**](ImageExportSpec.md) |  | 
**status** | [**ImageExportStatus**](ImageExportStatus.md) |  | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_export import ImageExport

# TODO update the JSON string below
json = "{}"
# create an instance of ImageExport from a JSON string
image_export_instance = ImageExport.from_json(json)
# print the JSON string representation of the object
print(ImageExport.to_json())

# convert the object into a dict
image_export_dict = image_export_instance.to_dict()
# create an instance of ImageExport from a dict
image_export_from_dict = ImageExport.from_dict(image_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


