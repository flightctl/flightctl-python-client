# DeviceSummaryStatus

A summary of the health of the device hardware and operating system resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeviceSummaryStatusType**](DeviceSummaryStatusType.md) |  | 
**info** | **str** | Human readable information detailing the last device status transition. | [optional] 

## Example

```python
from flightctl.models.device_summary_status import DeviceSummaryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSummaryStatus from a JSON string
device_summary_status_instance = DeviceSummaryStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceSummaryStatus.to_json())

# convert the object into a dict
device_summary_status_dict = device_summary_status_instance.to_dict()
# create an instance of DeviceSummaryStatus from a dict
device_summary_status_from_dict = DeviceSummaryStatus.from_dict(device_summary_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


