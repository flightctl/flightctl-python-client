# DiskResourceMonitorSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_rules** | [**List[ResourceAlertRule]**](ResourceAlertRule.md) | Array of alert rules. Only one alert per severity is allowed. | 
**sampling_interval** | **str** | Duration between monitor samples. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 
**monitor_type** | **str** | The type of resource to monitor. | 
**path** | **str** | The directory path to monitor for disk usage. | 

## Example

```python
from flightctl.models.disk_resource_monitor_spec import DiskResourceMonitorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DiskResourceMonitorSpec from a JSON string
disk_resource_monitor_spec_instance = DiskResourceMonitorSpec.from_json(json)
# print the JSON string representation of the object
print(DiskResourceMonitorSpec.to_json())

# convert the object into a dict
disk_resource_monitor_spec_dict = disk_resource_monitor_spec_instance.to_dict()
# create an instance of DiskResourceMonitorSpec from a dict
disk_resource_monitor_spec_from_dict = DiskResourceMonitorSpec.from_dict(disk_resource_monitor_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


