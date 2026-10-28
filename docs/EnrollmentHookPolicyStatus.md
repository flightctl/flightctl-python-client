# EnrollmentHookPolicyStatus

Status of an enrollment hook policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[Condition]**](Condition.md) | Current conditions of the enrollment hook policy. | [optional]

## Example

```python
from flightctl.models.enrollment_hook_policy_status import EnrollmentHookPolicyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookPolicyStatus from a JSON string
enrollment_hook_policy_status_instance = EnrollmentHookPolicyStatus.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookPolicyStatus.to_json())

# convert the object into a dict
enrollment_hook_policy_status_dict = enrollment_hook_policy_status_instance.to_dict()
# create an instance of EnrollmentHookPolicyStatus from a dict
enrollment_hook_policy_status_from_dict = EnrollmentHookPolicyStatus.from_dict(enrollment_hook_policy_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
