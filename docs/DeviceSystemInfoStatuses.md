# DeviceSystemInfoStatuses

Collection statuses for built-in and custom information sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_info** | [**Dict[str, SystemInfoSourceStatus]**](SystemInfoSourceStatus.md) | Per-source collection status for built-in system information. |
**custom_info** | [**Dict[str, SystemInfoSourceStatus]**](SystemInfoSourceStatus.md) | Per-source collection status for custom device information. |

## Example

```python
from flightctl.models.device_system_info_statuses import DeviceSystemInfoStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSystemInfoStatuses from a JSON string
device_system_info_statuses_instance = DeviceSystemInfoStatuses.from_json(json)
# print the JSON string representation of the object
print(DeviceSystemInfoStatuses.to_json())

# convert the object into a dict
device_system_info_statuses_dict = device_system_info_statuses_instance.to_dict()
# create an instance of DeviceSystemInfoStatuses from a dict
device_system_info_statuses_from_dict = DeviceSystemInfoStatuses.from_dict(device_system_info_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
