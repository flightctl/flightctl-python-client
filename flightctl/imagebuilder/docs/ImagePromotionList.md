# ImagePromotionList

ImagePromotionList is a list of ImagePromotion resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[ImagePromotion]**](ImagePromotion.md) | List of ImagePromotion resources. | 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_list import ImagePromotionList

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionList from a JSON string
image_promotion_list_instance = ImagePromotionList.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionList.to_json())

# convert the object into a dict
image_promotion_list_dict = image_promotion_list_instance.to_dict()
# create an instance of ImagePromotionList from a dict
image_promotion_list_from_dict = ImagePromotionList.from_dict(image_promotion_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


