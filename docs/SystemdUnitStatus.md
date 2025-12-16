# SystemdUnitStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit name (e.g., \&quot;sshd.service\&quot;). | 
**description** | **str** | The human-readable description for the unit. | 
**enable_state** | [**SystemdEnableStateType**](SystemdEnableStateType.md) |  | 
**load_state** | [**SystemdLoadStateType**](SystemdLoadStateType.md) |  | 
**active_state** | [**SystemdActiveStateType**](SystemdActiveStateType.md) |  | 
**sub_state** | **str** | The low-level, unit-type-specific state. | 

## Example

```python
from flightctl.models.systemd_unit_status import SystemdUnitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SystemdUnitStatus from a JSON string
systemd_unit_status_instance = SystemdUnitStatus.from_json(json)
# print the JSON string representation of the object
print(SystemdUnitStatus.to_json())

# convert the object into a dict
systemd_unit_status_dict = systemd_unit_status_instance.to_dict()
# create an instance of SystemdUnitStatus from a dict
systemd_unit_status_from_dict = SystemdUnitStatus.from_dict(systemd_unit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


