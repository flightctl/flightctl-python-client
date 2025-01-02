# RolloutPolicy

RolloutPolicy is the rollout policy of the fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_allowance** | [**DisruptionAllowance**](DisruptionAllowance.md) |  | [optional] 
**device_selection** | [**RolloutDeviceSelection**](RolloutDeviceSelection.md) |  | [optional] 
**success_threshold** | **str** | Percentage is the string format representing percentage string. | [optional] 
**default_update_timeout** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: &#x60;s&#x60; for seconds, &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours. | [optional] [default to '0s']

## Example

```python
from flightctl.models.rollout_policy import RolloutPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RolloutPolicy from a JSON string
rollout_policy_instance = RolloutPolicy.from_json(json)
# print the JSON string representation of the object
print(RolloutPolicy.to_json())

# convert the object into a dict
rollout_policy_dict = rollout_policy_instance.to_dict()
# create an instance of RolloutPolicy from a dict
rollout_policy_from_dict = RolloutPolicy.from_dict(rollout_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


