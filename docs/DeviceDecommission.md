# DeviceDecommission

Metadata about a device decommissioning request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**DeviceDecommissionTargetType**](DeviceDecommissionTargetType.md) |  | 

## Example

```python
from flightctl.models.device_decommission import DeviceDecommission

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDecommission from a JSON string
device_decommission_instance = DeviceDecommission.from_json(json)
# print the JSON string representation of the object
print(DeviceDecommission.to_json())

# convert the object into a dict
device_decommission_dict = device_decommission_instance.to_dict()
# create an instance of DeviceDecommission from a dict
device_decommission_from_dict = DeviceDecommission.from_dict(device_decommission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


