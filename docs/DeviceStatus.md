# DeviceStatus

DeviceStatus represents information about the status of a device. Status may trail the actual state of a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[Condition]**](Condition.md) | Conditions represent the observations of a the current state of a device. | 
**system_info** | [**DeviceSystemInfo**](DeviceSystemInfo.md) |  | 
**applications** | [**List[DeviceApplicationStatus]**](DeviceApplicationStatus.md) | List of device application status. | 
**applications_summary** | [**DeviceApplicationsSummaryStatus**](DeviceApplicationsSummaryStatus.md) |  | 
**resources** | [**DeviceResourceStatus**](DeviceResourceStatus.md) |  | 
**integrity** | [**DeviceIntegrityStatus**](DeviceIntegrityStatus.md) |  | 
**config** | [**DeviceConfigStatus**](DeviceConfigStatus.md) |  | 
**os** | [**DeviceOsStatus**](DeviceOsStatus.md) |  | 
**updated** | [**DeviceUpdatedStatus**](DeviceUpdatedStatus.md) |  | 
**summary** | [**DeviceSummaryStatus**](DeviceSummaryStatus.md) |  | 
**last_seen** | **datetime** | The last time the device was seen by the service. | 
**lifecycle** | [**DeviceLifecycleStatus**](DeviceLifecycleStatus.md) |  | 

## Example

```python
from flightctl.models.device_status import DeviceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatus from a JSON string
device_status_instance = DeviceStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceStatus.to_json())

# convert the object into a dict
device_status_dict = device_status_instance.to_dict()
# create an instance of DeviceStatus from a dict
device_status_from_dict = DeviceStatus.from_dict(device_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


