# ImagePromotionSource

Identifies the artifact(s) to publish.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_build_ref** | **str** | Name of the ImageBuild resource this promotion is linked to. The container/bootc artifact produced by this build is always included in the CatalogItem version entry. | 
**export_formats** | [**List[ExportFormatType]**](ExportFormatType.md) | Optional list of additional artifact formats to include in the CatalogItem version entry. The promotion waits in WaitingForArtifacts until at least one successful ImageExport exists for every requested format. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_source import ImagePromotionSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionSource from a JSON string
image_promotion_source_instance = ImagePromotionSource.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionSource.to_json())

# convert the object into a dict
image_promotion_source_dict = image_promotion_source_instance.to_dict()
# create an instance of ImagePromotionSource from a dict
image_promotion_source_from_dict = ImagePromotionSource.from_dict(image_promotion_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


