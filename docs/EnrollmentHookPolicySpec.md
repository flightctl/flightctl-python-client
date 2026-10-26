# EnrollmentHookPolicySpec

Specification for an enrollment hook policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_enrolling** | [**EnrollmentHookStageSpec**](EnrollmentHookStageSpec.md) |  |

## Example

```python
from flightctl.models.enrollment_hook_policy_spec import EnrollmentHookPolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookPolicySpec from a JSON string
enrollment_hook_policy_spec_instance = EnrollmentHookPolicySpec.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookPolicySpec.to_json())

# convert the object into a dict
enrollment_hook_policy_spec_dict = enrollment_hook_policy_spec_instance.to_dict()
# create an instance of EnrollmentHookPolicySpec from a dict
enrollment_hook_policy_spec_from_dict = EnrollmentHookPolicySpec.from_dict(enrollment_hook_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
