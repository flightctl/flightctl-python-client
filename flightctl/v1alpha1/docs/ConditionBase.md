# ConditionBase

Base condition structure following Kubernetes API conventions. Use with allOf to add a specific type enum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConditionStatus**](ConditionStatus.md) |  | 
**observed_generation** | **int** | The .metadata.generation that the condition was set based upon. | [optional] 
**last_transition_time** | **datetime** | The last time the condition transitioned from one status to another. | 
**message** | **str** | Human readable message indicating details about last transition. | 
**reason** | **str** | A (brief) reason for the condition&#39;s last transition. | 

## Example

```python
from flightctl.v1alpha1.models.condition_base import ConditionBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionBase from a JSON string
condition_base_instance = ConditionBase.from_json(json)
# print the JSON string representation of the object
print(ConditionBase.to_json())

# convert the object into a dict
condition_base_dict = condition_base_instance.to_dict()
# create an instance of ConditionBase from a dict
condition_base_from_dict = ConditionBase.from_dict(condition_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


