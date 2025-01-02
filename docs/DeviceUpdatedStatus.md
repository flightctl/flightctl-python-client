# DeviceUpdatedStatus

Current status of the device update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeviceUpdatedStatusType**](DeviceUpdatedStatusType.md) |  | 
**info** | **str** | Human readable information about the last device update transition. | [optional] 

## Example

```python
from flightctl.models.device_updated_status import DeviceUpdatedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUpdatedStatus from a JSON string
device_updated_status_instance = DeviceUpdatedStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceUpdatedStatus.to_json())

# convert the object into a dict
device_updated_status_dict = device_updated_status_instance.to_dict()
# create an instance of DeviceUpdatedStatus from a dict
device_updated_status_from_dict = DeviceUpdatedStatus.from_dict(device_updated_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


