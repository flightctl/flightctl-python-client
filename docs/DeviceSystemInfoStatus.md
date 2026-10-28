# DeviceSystemInfoStatus

Status of the system information collection sources for a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**DeviceSystemInfoSummaryStatus**](DeviceSystemInfoSummaryStatus.md) |  |
**statuses** | [**DeviceSystemInfoStatuses**](DeviceSystemInfoStatuses.md) |  |

## Example

```python
from flightctl.models.device_system_info_status import DeviceSystemInfoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSystemInfoStatus from a JSON string
device_system_info_status_instance = DeviceSystemInfoStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceSystemInfoStatus.to_json())

# convert the object into a dict
device_system_info_status_dict = device_system_info_status_instance.to_dict()
# create an instance of DeviceSystemInfoStatus from a dict
device_system_info_status_from_dict = DeviceSystemInfoStatus.from_dict(device_system_info_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
