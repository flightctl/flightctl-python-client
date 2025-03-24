# DeviceResourceStatus

Current status of the resources of the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**DeviceResourceStatusType**](DeviceResourceStatusType.md) |  | 
**memory** | [**DeviceResourceStatusType**](DeviceResourceStatusType.md) |  | 
**disk** | [**DeviceResourceStatusType**](DeviceResourceStatusType.md) |  | 

## Example

```python
from flightctl.models.device_resource_status import DeviceResourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceResourceStatus from a JSON string
device_resource_status_instance = DeviceResourceStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceResourceStatus.to_json())

# convert the object into a dict
device_resource_status_dict = device_resource_status_instance.to_dict()
# create an instance of DeviceResourceStatus from a dict
device_resource_status_from_dict = DeviceResourceStatus.from_dict(device_resource_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


