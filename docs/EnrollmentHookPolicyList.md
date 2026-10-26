# EnrollmentHookPolicyList

EnrollmentHookPolicyList is a list of EnrollmentHookPolicy resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  |
**kind** | **str** | Kind is a string value representing the REST resource this object represents. |
**metadata** | [**ListMeta**](ListMeta.md) |  |
**items** | [**List[EnrollmentHookPolicy]**](EnrollmentHookPolicy.md) | List of enrollment hook policies. |

## Example

```python
from flightctl.models.enrollment_hook_policy_list import EnrollmentHookPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookPolicyList from a JSON string
enrollment_hook_policy_list_instance = EnrollmentHookPolicyList.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookPolicyList.to_json())

# convert the object into a dict
enrollment_hook_policy_list_dict = enrollment_hook_policy_list_instance.to_dict()
# create an instance of EnrollmentHookPolicyList from a dict
enrollment_hook_policy_list_from_dict = EnrollmentHookPolicyList.from_dict(enrollment_hook_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
