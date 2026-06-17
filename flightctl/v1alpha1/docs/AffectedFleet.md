# AffectedFleet

One fleet or the fleetless aggregate with device and image counts for a CVE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet_name** | **str** | Fleet metadata.name, empty for the fleetless aggregate. | 
**fleetless** | **bool** | True when this row represents devices not owned by a fleet. | 
**affected_devices** | **int** | Devices in this fleet or fleetless group affected by the CVE. | 
**findings** | [**List[VulnerabilityGroupItem]**](VulnerabilityGroupItem.md) | Per-digest findings within this fleet or fleetless group. | 

## Example

```python
from flightctl.v1alpha1.models.affected_fleet import AffectedFleet

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedFleet from a JSON string
affected_fleet_instance = AffectedFleet.from_json(json)
# print the JSON string representation of the object
print(AffectedFleet.to_json())

# convert the object into a dict
affected_fleet_dict = affected_fleet_instance.to_dict()
# create an instance of AffectedFleet from a dict
affected_fleet_from_dict = AffectedFleet.from_dict(affected_fleet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


