# CustomResourceMonitorSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of resource to monitor. | 
**alert_rules** | [**List[ResourceAlertRule]**](ResourceAlertRule.md) | Array of alert rules. Only one alert per severity is allowed. | 
**sampling_interval** | **str** | Duration between monitor samples. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 

## Example

```python
from flightctl.models.custom_resource_monitor_spec import CustomResourceMonitorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CustomResourceMonitorSpec from a JSON string
custom_resource_monitor_spec_instance = CustomResourceMonitorSpec.from_json(json)
# print the JSON string representation of the object
print(CustomResourceMonitorSpec.to_json())

# convert the object into a dict
custom_resource_monitor_spec_dict = custom_resource_monitor_spec_instance.to_dict()
# create an instance of CustomResourceMonitorSpec from a dict
custom_resource_monitor_spec_from_dict = CustomResourceMonitorSpec.from_dict(custom_resource_monitor_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


