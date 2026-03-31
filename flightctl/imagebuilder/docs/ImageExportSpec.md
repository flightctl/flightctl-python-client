# ImageExportSpec

ImageExportSpec describes the specification for an image export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ImageBuildRefSource**](ImageBuildRefSource.md) |  | 
**format** | [**ExportFormatType**](ExportFormatType.md) |  | 

## Example

```python
from flightctl.imagebuilder.models.image_export_spec import ImageExportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageExportSpec from a JSON string
image_export_spec_instance = ImageExportSpec.from_json(json)
# print the JSON string representation of the object
print(ImageExportSpec.to_json())

# convert the object into a dict
image_export_spec_dict = image_export_spec_instance.to_dict()
# create an instance of ImageExportSpec from a dict
image_export_spec_from_dict = ImageExportSpec.from_dict(image_export_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


