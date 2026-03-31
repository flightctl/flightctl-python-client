# ImageExportStatus

ImageExportStatus represents the current status of an ImageExport.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[ImageExportCondition]**](ImageExportCondition.md) | Current conditions of the ImageExport. | [optional] 
**manifest_digest** | **str** | The digest of the exported image manifest for this format. | [optional] 
**last_seen** | **datetime** | The last time the export was seen (heartbeat). | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_export_status import ImageExportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ImageExportStatus from a JSON string
image_export_status_instance = ImageExportStatus.from_json(json)
# print the JSON string representation of the object
print(ImageExportStatus.to_json())

# convert the object into a dict
image_export_status_dict = image_export_status_instance.to_dict()
# create an instance of ImageExportStatus from a dict
image_export_status_from_dict = ImageExportStatus.from_dict(image_export_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


