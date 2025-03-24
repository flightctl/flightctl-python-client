# FleetRolloutStatus

FleetRolloutStatus represents information about the status of a fleet rollout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_batch** | **int** | The batch number currently being rolled out. | [optional] 

## Example

```python
from flightctl.models.fleet_rollout_status import FleetRolloutStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutStatus from a JSON string
fleet_rollout_status_instance = FleetRolloutStatus.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutStatus.to_json())

# convert the object into a dict
fleet_rollout_status_dict = fleet_rollout_status_instance.to_dict()
# create an instance of FleetRolloutStatus from a dict
fleet_rollout_status_from_dict = FleetRolloutStatus.from_dict(fleet_rollout_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


