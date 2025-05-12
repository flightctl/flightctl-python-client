# DeviceSystemInfo

System information collected from the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The Architecture reported by the device. | 
**boot_id** | **str** | Boot ID reported by the device. | 
**operating_system** | **str** | The Operating System reported by the device. | 
**agent_version** | **str** | The Agent version. | 
**custom_info** | **Dict[str, str]** | User-defined information about the device. | [optional] 

## Example

```python
from flightctl.models.device_system_info import DeviceSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSystemInfo from a JSON string
device_system_info_instance = DeviceSystemInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceSystemInfo.to_json())

# convert the object into a dict
device_system_info_dict = device_system_info_instance.to_dict()
# create an instance of DeviceSystemInfo from a dict
device_system_info_from_dict = DeviceSystemInfo.from_dict(device_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


