# DeviceApplicationsSummaryStatus

A summary of the health of applications on the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ApplicationsSummaryStatusType**](ApplicationsSummaryStatusType.md) |  | 
**info** | **str** | Human readable information detailing the last application transition. | [optional] 

## Example

```python
from flightctl.models.device_applications_summary_status import DeviceApplicationsSummaryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceApplicationsSummaryStatus from a JSON string
device_applications_summary_status_instance = DeviceApplicationsSummaryStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceApplicationsSummaryStatus.to_json())

# convert the object into a dict
device_applications_summary_status_dict = device_applications_summary_status_instance.to_dict()
# create an instance of DeviceApplicationsSummaryStatus from a dict
device_applications_summary_status_from_dict = DeviceApplicationsSummaryStatus.from_dict(device_applications_summary_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


