# DeviceUpdatePolicySpec

Specifies the policy for managing device updates, including when updates should be downloaded and applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_schedule** | [**UpdateSchedule**](UpdateSchedule.md) |  | [optional] 
**update_schedule** | [**UpdateSchedule**](UpdateSchedule.md) |  | [optional] 

## Example

```python
from flightctl.models.device_update_policy_spec import DeviceUpdatePolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUpdatePolicySpec from a JSON string
device_update_policy_spec_instance = DeviceUpdatePolicySpec.from_json(json)
# print the JSON string representation of the object
print(DeviceUpdatePolicySpec.to_json())

# convert the object into a dict
device_update_policy_spec_dict = device_update_policy_spec_instance.to_dict()
# create an instance of DeviceUpdatePolicySpec from a dict
device_update_policy_spec_from_dict = DeviceUpdatePolicySpec.from_dict(device_update_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


