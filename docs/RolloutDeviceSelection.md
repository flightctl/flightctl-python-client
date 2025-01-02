# RolloutDeviceSelection

Describes how to select devices for rollout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | The rollout strategy to use. | 
**sequence** | [**List[Batch]**](Batch.md) | A list of batch definitions. | [optional] 

## Example

```python
from flightctl.models.rollout_device_selection import RolloutDeviceSelection

# TODO update the JSON string below
json = "{}"
# create an instance of RolloutDeviceSelection from a JSON string
rollout_device_selection_instance = RolloutDeviceSelection.from_json(json)
# print the JSON string representation of the object
print(RolloutDeviceSelection.to_json())

# convert the object into a dict
rollout_device_selection_dict = rollout_device_selection_instance.to_dict()
# create an instance of RolloutDeviceSelection from a dict
rollout_device_selection_from_dict = RolloutDeviceSelection.from_dict(rollout_device_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


