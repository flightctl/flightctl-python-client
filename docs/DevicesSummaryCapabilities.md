# DevicesSummaryCapabilities

Breakdowns of devices by status.systemInfo fields, falling back to the deprecated status.capabilities fields when unavailable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_mode** | **Dict[str, int]** | Counts by device OS mode (e.g. image, package), taken from status.systemInfo.osMode with fallback to the deprecated status.capabilities.osMode. The key \&quot;unknown\&quot; counts devices that have not reported an OS mode. | [optional]

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


