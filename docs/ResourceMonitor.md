# ResourceMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of resource to monitor. | 
**alert_rules** | [**List[ResourceAlertRule]**](ResourceAlertRule.md) | Array of alert rules. Only one alert per severity is allowed. | 
**sampling_interval** | **str** | Duration between monitor samples. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 
**path** | **str** | The directory path to monitor for disk usage. | 

## Example

```python
from flightctl.models.resource_monitor import ResourceMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMonitor from a JSON string
resource_monitor_instance = ResourceMonitor.from_json(json)
# print the JSON string representation of the object
print(ResourceMonitor.to_json())

# convert the object into a dict
resource_monitor_dict = resource_monitor_instance.to_dict()
# create an instance of ResourceMonitor from a dict
resource_monitor_from_dict = ResourceMonitor.from_dict(resource_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


