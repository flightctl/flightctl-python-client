# DeviceSystemInfoSummaryStatus

Aggregate summary of the system information collection health.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SystemInfoSummaryStatusType**](SystemInfoSummaryStatusType.md) |  |

## Example

```python
from flightctl.models.device_system_info_summary_status import DeviceSystemInfoSummaryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSystemInfoSummaryStatus from a JSON string
device_system_info_summary_status_instance = DeviceSystemInfoSummaryStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceSystemInfoSummaryStatus.to_json())

# convert the object into a dict
device_system_info_summary_status_dict = device_system_info_summary_status_instance.to_dict()
# create an instance of DeviceSystemInfoSummaryStatus from a dict
device_system_info_summary_status_from_dict = DeviceSystemInfoSummaryStatus.from_dict(device_system_info_summary_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
