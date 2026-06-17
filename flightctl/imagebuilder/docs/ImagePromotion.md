# ImagePromotion

ImagePromotion tracks a single publish attempt from an ImageBuild to a CatalogItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**ImagePromotionSpec**](ImagePromotionSpec.md) |  | 
**status** | [**ImagePromotionStatus**](ImagePromotionStatus.md) |  | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_promotion import ImagePromotion

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotion from a JSON string
image_promotion_instance = ImagePromotion.from_json(json)
# print the JSON string representation of the object
print(ImagePromotion.to_json())

# convert the object into a dict
image_promotion_dict = image_promotion_instance.to_dict()
# create an instance of ImagePromotion from a dict
image_promotion_from_dict = ImagePromotion.from_dict(image_promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


