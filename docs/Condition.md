# Condition

Condition contains details for one aspect of the current state of this API Resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConditionType**](ConditionType.md) |  | 
**status** | [**ConditionStatus**](ConditionStatus.md) |  | 
**observed_generation** | **int** | The .metadata.generation that the condition was set based upon. | [optional] 
**last_transition_time** | **datetime** | The last time the condition transitioned from one status to another. | 
**message** | **str** | Human readable message indicating details about last transition. | 
**reason** | **str** | A (brief) reason for the condition&#39;s last transition. | 

## Example

```python
from flightctl.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print(Condition.to_json())

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_from_dict = Condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


