# MemoryResourceMonitorSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of resource to monitor. | 
**alert_rules** | [**List[ResourceAlertRule]**](ResourceAlertRule.md) | Array of alert rules. Only one alert per severity is allowed. | 
**sampling_interval** | **str** | Duration between monitor samples. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 

## Example

```python
from flightctl.models.memory_resource_monitor_spec import MemoryResourceMonitorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryResourceMonitorSpec from a JSON string
memory_resource_monitor_spec_instance = MemoryResourceMonitorSpec.from_json(json)
# print the JSON string representation of the object
print(MemoryResourceMonitorSpec.to_json())

# convert the object into a dict
memory_resource_monitor_spec_dict = memory_resource_monitor_spec_instance.to_dict()
# create an instance of MemoryResourceMonitorSpec from a dict
memory_resource_monitor_spec_from_dict = MemoryResourceMonitorSpec.from_dict(memory_resource_monitor_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


