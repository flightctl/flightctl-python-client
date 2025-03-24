# CpuResourceMonitorSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of resource to monitor. | 
**alert_rules** | [**List[ResourceAlertRule]**](ResourceAlertRule.md) | Array of alert rules. Only one alert per severity is allowed. | 
**sampling_interval** | **str** | Duration between monitor samples. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 

## Example

```python
from flightctl.models.cpu_resource_monitor_spec import CpuResourceMonitorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CpuResourceMonitorSpec from a JSON string
cpu_resource_monitor_spec_instance = CpuResourceMonitorSpec.from_json(json)
# print the JSON string representation of the object
print(CpuResourceMonitorSpec.to_json())

# convert the object into a dict
cpu_resource_monitor_spec_dict = cpu_resource_monitor_spec_instance.to_dict()
# create an instance of CpuResourceMonitorSpec from a dict
cpu_resource_monitor_spec_from_dict = CpuResourceMonitorSpec.from_dict(cpu_resource_monitor_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


