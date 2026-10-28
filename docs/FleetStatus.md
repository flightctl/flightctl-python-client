# FleetStatus

FleetStatus represents information about the status of a fleet. Status may trail the actual state of a fleet, especially if devices of a fleet have not contacted the management service in a while.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollout** | [**FleetRolloutStatus**](FleetRolloutStatus.md) |  | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | Current state of the fleet. | 
**devices_summary** | [**DevicesSummary**](DevicesSummary.md) |  | [optional] 
**delta_generation** | [**DeltaGenerationStatus**](DeltaGenerationStatus.md) |  | [optional]

## Example

```python
from flightctl.models.fleet_status import FleetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FleetStatus from a JSON string
fleet_status_instance = FleetStatus.from_json(json)
# print the JSON string representation of the object
print(FleetStatus.to_json())

# convert the object into a dict
fleet_status_dict = fleet_status_instance.to_dict()
# create an instance of FleetStatus from a dict
fleet_status_from_dict = FleetStatus.from_dict(fleet_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


