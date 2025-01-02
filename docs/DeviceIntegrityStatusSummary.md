# DeviceIntegrityStatusSummary

Summary status of the integrity of the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeviceIntegrityStatusSummaryType**](DeviceIntegrityStatusSummaryType.md) |  | 
**info** | **str** | Human readable information about the last integrity transition. | [optional] 

## Example

```python
from flightctl.models.device_integrity_status_summary import DeviceIntegrityStatusSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrityStatusSummary from a JSON string
device_integrity_status_summary_instance = DeviceIntegrityStatusSummary.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrityStatusSummary.to_json())

# convert the object into a dict
device_integrity_status_summary_dict = device_integrity_status_summary_instance.to_dict()
# create an instance of DeviceIntegrityStatusSummary from a dict
device_integrity_status_summary_from_dict = DeviceIntegrityStatusSummary.from_dict(device_integrity_status_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


