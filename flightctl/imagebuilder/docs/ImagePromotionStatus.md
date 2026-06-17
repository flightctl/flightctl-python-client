# ImagePromotionStatus

Observed state of an ImagePromotion resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[ImagePromotionCondition]**](ImagePromotionCondition.md) | Conditions describing the current state of the promotion lifecycle. | [optional] 
**published_at** | **datetime** | Timestamp of the initial successful promotion. Set once when the promotion first reaches Completed state. Not updated by subsequent amendments. | [optional] 
**last_amended_at** | **datetime** | Timestamp of the most recent successful amendment (i.e., when the last additional export format was written to the CatalogItemVersion). Absent if the promotion has never been amended. | [optional] 
**artifact_statuses** | [**List[ArtifactPromotionStatus]**](ArtifactPromotionStatus.md) | Per-artifact readiness summary. One entry for the ImageBuild (container artifact) and one entry per requested exportFormat. Updated as artifacts become available or as new formats are added via PATCH/PUT. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_status import ImagePromotionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionStatus from a JSON string
image_promotion_status_instance = ImagePromotionStatus.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionStatus.to_json())

# convert the object into a dict
image_promotion_status_dict = image_promotion_status_instance.to_dict()
# create an instance of ImagePromotionStatus from a dict
image_promotion_status_from_dict = ImagePromotionStatus.from_dict(image_promotion_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


