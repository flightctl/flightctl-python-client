# EnrollmentHookAuth

Authentication configuration for an enrollment hook action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** | Bearer token for HTTP authentication. | [optional]

## Example

```python
from flightctl.models.enrollment_hook_auth import EnrollmentHookAuth

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookAuth from a JSON string
enrollment_hook_auth_instance = EnrollmentHookAuth.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookAuth.to_json())

# convert the object into a dict
enrollment_hook_auth_dict = enrollment_hook_auth_instance.to_dict()
# create an instance of EnrollmentHookAuth from a dict
enrollment_hook_auth_from_dict = EnrollmentHookAuth.from_dict(enrollment_hook_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
