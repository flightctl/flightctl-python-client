# ImagePromotionSpec

Desired state of an ImagePromotion resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ImagePromotionSource**](ImagePromotionSource.md) |  | 
**target** | [**ImagePromotionTarget**](ImagePromotionTarget.md) |  | 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_spec import ImagePromotionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionSpec from a JSON string
image_promotion_spec_instance = ImagePromotionSpec.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionSpec.to_json())

# convert the object into a dict
image_promotion_spec_dict = image_promotion_spec_instance.to_dict()
# create an instance of ImagePromotionSpec from a dict
image_promotion_spec_from_dict = ImagePromotionSpec.from_dict(image_promotion_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


