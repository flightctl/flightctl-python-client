# ImagePromotionCondition

Condition for ImagePromotion resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConditionStatus**](ConditionStatus.md) |  | 
**observed_generation** | **int** | The .metadata.generation that the condition was set based upon. | [optional] 
**last_transition_time** | **datetime** | The last time the condition transitioned from one status to another. | 
**message** | **str** | Human readable message indicating details about last transition. | 
**reason** | **str** | A (brief) reason for the condition&#39;s last transition. | 
**type** | [**ImagePromotionConditionType**](ImagePromotionConditionType.md) |  | 

## Example

```python
from flightctl.imagebuilder.models.image_promotion_condition import ImagePromotionCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromotionCondition from a JSON string
image_promotion_condition_instance = ImagePromotionCondition.from_json(json)
# print the JSON string representation of the object
print(ImagePromotionCondition.to_json())

# convert the object into a dict
image_promotion_condition_dict = image_promotion_condition_instance.to_dict()
# create an instance of ImagePromotionCondition from a dict
image_promotion_condition_from_dict = ImagePromotionCondition.from_dict(image_promotion_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


