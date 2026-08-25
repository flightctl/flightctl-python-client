# DevicesSummaryCapabilities

Breakdowns of devices by status.capabilities fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_mode** | **Dict[str, int]** | Counts by status.capabilities.osMode (e.g. image, package). The key \&quot;unknown\&quot; counts devices that have not reported the capability. | [optional] 

## Example

```python
from flightctl.models.devices_summary_capabilities import DevicesSummaryCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesSummaryCapabilities from a JSON string
devices_summary_capabilities_instance = DevicesSummaryCapabilities.from_json(json)
# print the JSON string representation of the object
print(DevicesSummaryCapabilities.to_json())

# convert the object into a dict
devices_summary_capabilities_dict = devices_summary_capabilities_instance.to_dict()
# create an instance of DevicesSummaryCapabilities from a dict
devices_summary_capabilities_from_dict = DevicesSummaryCapabilities.from_dict(devices_summary_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


