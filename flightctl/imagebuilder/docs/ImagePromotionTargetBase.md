# ImagePromotionTargetBase

Common fields shared by all ImagePromotionTarget variants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the target type. | 
**catalog_name** | **str** | Name of the parent Catalog resource. | 
**catalog_item_name** | **str** | Name of the CatalogItem to create or update. | 
**version** | **str** | Semver version string for the new CatalogItem version entry. | 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_target_base import ImagePromotionTargetBase

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionTargetBase from a JSON string
image_promotion_target_base_instance = ImagePromotionTargetBase.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionTargetBase.to_json())

# convert the object into a dict
image_promotion_target_base_dict = image_promotion_target_base_instance.to_dict()
# create an instance of ImagePromotionTargetBase from a dict
image_promotion_target_base_from_dict = ImagePromotionTargetBase.from_dict(image_promotion_target_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


