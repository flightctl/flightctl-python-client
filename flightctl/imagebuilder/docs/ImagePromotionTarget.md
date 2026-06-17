# ImagePromotionTarget

Specifies where and how to publish the artifact(s). The type field is the discriminator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the target type. | 
**catalog_name** | **str** | Name of the parent Catalog resource. | 
**catalog_item_name** | **str** | Name of the CatalogItem to update. | 
**version** | **str** | Semver version string for the new CatalogItem version entry. | 
**readme** | **str** | Optional version-level readme for this version entry. Markdown is supported. | [optional] 
**display_name** | **str** | Optional human-readable display name for the new CatalogItem. | [optional] 
**replaces** | **str** | The single version this one replaces, defining the primary upgrade edge. | [optional] 
**skips** | **List[str]** | Additional versions that can upgrade directly to this one. | [optional] 
**skip_range** | **str** | Semver range of versions that can upgrade directly to this one (e.g. \&quot;&gt;&#x3D;1.0.0 &lt;1.3.0\&quot;). | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_target import ImagePromotionTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionTarget from a JSON string
image_promotion_target_instance = ImagePromotionTarget.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionTarget.to_json())

# convert the object into a dict
image_promotion_target_dict = image_promotion_target_instance.to_dict()
# create an instance of ImagePromotionTarget from a dict
image_promotion_target_from_dict = ImagePromotionTarget.from_dict(image_promotion_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


