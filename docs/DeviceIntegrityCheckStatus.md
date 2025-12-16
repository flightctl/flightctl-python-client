# DeviceIntegrityCheckStatus

DeviceIntegrityCheckStatus represents the status of the integrity check performed on the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeviceIntegrityCheckStatusType**](DeviceIntegrityCheckStatusType.md) |  | 
**info** | **str** | Human-readable information about the integrity check status. | [optional] 

## Example

```python
from flightctl.models.device_integrity_check_status import DeviceIntegrityCheckStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrityCheckStatus from a JSON string
device_integrity_check_status_instance = DeviceIntegrityCheckStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrityCheckStatus.to_json())

# convert the object into a dict
device_integrity_check_status_dict = device_integrity_check_status_instance.to_dict()
# create an instance of DeviceIntegrityCheckStatus from a dict
device_integrity_check_status_from_dict = DeviceIntegrityCheckStatus.from_dict(device_integrity_check_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


