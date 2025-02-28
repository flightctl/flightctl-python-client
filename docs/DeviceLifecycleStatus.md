# DeviceLifecycleStatus

Current status of the device lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeviceLifecycleStatusType**](DeviceLifecycleStatusType.md) |  | 
**info** | **str** | Human readable information about the device lifecycle status. | [optional] 

## Example

```python
from flightctl.models.device_lifecycle_status import DeviceLifecycleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleStatus from a JSON string
device_lifecycle_status_instance = DeviceLifecycleStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceLifecycleStatus.to_json())

# convert the object into a dict
device_lifecycle_status_dict = device_lifecycle_status_instance.to_dict()
# create an instance of DeviceLifecycleStatus from a dict
device_lifecycle_status_from_dict = DeviceLifecycleStatus.from_dict(device_lifecycle_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


