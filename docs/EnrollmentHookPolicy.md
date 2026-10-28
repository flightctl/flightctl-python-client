# EnrollmentHookPolicy

EnrollmentHookPolicy defines an org-scoped enrollment hook policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  |
**kind** | **str** | Kind is a string value representing the REST resource this object represents. |
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |
**spec** | [**EnrollmentHookPolicySpec**](EnrollmentHookPolicySpec.md) |  |
**status** | [**EnrollmentHookPolicyStatus**](EnrollmentHookPolicyStatus.md) |  | [optional]

## Example

```python
from flightctl.models.enrollment_hook_policy import EnrollmentHookPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookPolicy from a JSON string
enrollment_hook_policy_instance = EnrollmentHookPolicy.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookPolicy.to_json())

# convert the object into a dict
enrollment_hook_policy_dict = enrollment_hook_policy_instance.to_dict()
# create an instance of EnrollmentHookPolicy from a dict
enrollment_hook_policy_from_dict = EnrollmentHookPolicy.from_dict(enrollment_hook_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
