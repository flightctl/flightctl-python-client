# DevicesSummary

A summary of the devices in the fleet returned when fetching a single Fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of devices in the fleet. | 
**application_status** | **Dict[str, int]** | A breakdown of the devices in the fleet by \&quot;application\&quot; status. | [optional] 
**summary_status** | **Dict[str, int]** | A breakdown of the devices in the fleet by \&quot;summary\&quot; status. | [optional] 
**update_status** | **Dict[str, int]** | A breakdown of the devices in the fleet by \&quot;updated\&quot; status. | [optional] 

## Example

```python
from flightctl.models.devices_summary import DevicesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesSummary from a JSON string
devices_summary_instance = DevicesSummary.from_json(json)
# print the JSON string representation of the object
print(DevicesSummary.to_json())

# convert the object into a dict
devices_summary_dict = devices_summary_instance.to_dict()
# create an instance of DevicesSummary from a dict
devices_summary_from_dict = DevicesSummary.from_dict(devices_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


