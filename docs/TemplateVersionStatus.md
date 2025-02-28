# TemplateVersionStatus

TemplateVersionStatus represents information about the status of a template version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_policy** | [**DeviceUpdatePolicySpec**](DeviceUpdatePolicySpec.md) |  | [optional] 
**os** | [**DeviceOsSpec**](DeviceOsSpec.md) |  | [optional] 
**config** | [**List[ConfigProviderSpec]**](ConfigProviderSpec.md) | List of config providers. | [optional] 
**applications** | [**List[ApplicationProviderSpec]**](ApplicationProviderSpec.md) | List of application providers. | [optional] 
**systemd** | [**DeviceSpecSystemd**](DeviceSpecSystemd.md) |  | [optional] 
**resources** | [**List[ResourceMonitor]**](ResourceMonitor.md) | Array of resource monitor configurations. | [optional] 
**consoles** | [**List[DeviceConsole]**](DeviceConsole.md) | The list of active console sessions. | [optional] 
**decommissioning** | [**DeviceDecommission**](DeviceDecommission.md) |  | [optional] 
**updated_at** | **datetime** | The time at which the template was last updated. | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | Current state of the device. | 

## Example

```python
from flightctl.models.template_version_status import TemplateVersionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionStatus from a JSON string
template_version_status_instance = TemplateVersionStatus.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionStatus.to_json())

# convert the object into a dict
template_version_status_dict = template_version_status_instance.to_dict()
# create an instance of TemplateVersionStatus from a dict
template_version_status_from_dict = TemplateVersionStatus.from_dict(template_version_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


