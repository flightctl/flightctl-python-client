# EnrollmentHookStageSpec

Configuration for a stage of enrollment hooks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_policy** | [**FailurePolicyType**](FailurePolicyType.md) |  | [optional]
**control_plane_actions** | [**List[EnrollmentHookHttpAction]**](EnrollmentHookHttpAction.md) | List of HTTP actions to execute during this enrollment stage. | [optional]

## Example

```python
from flightctl.models.enrollment_hook_stage_spec import EnrollmentHookStageSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookStageSpec from a JSON string
enrollment_hook_stage_spec_instance = EnrollmentHookStageSpec.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookStageSpec.to_json())

# convert the object into a dict
enrollment_hook_stage_spec_dict = enrollment_hook_stage_spec_instance.to_dict()
# create an instance of EnrollmentHookStageSpec from a dict
enrollment_hook_stage_spec_from_dict = EnrollmentHookStageSpec.from_dict(enrollment_hook_stage_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
