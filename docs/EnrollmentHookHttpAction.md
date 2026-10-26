# EnrollmentHookHttpAction

An HTTP action to execute as part of an enrollment hook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTPS URL to call. |
**timeout** | **str** | Timeout duration (e.g. \&quot;30s\&quot;). Defaults to 30s, max 5m. | [optional]
**retry** | [**EnrollmentHookRetryPolicy**](EnrollmentHookRetryPolicy.md) |  | [optional]
**auth** | [**EnrollmentHookAuth**](EnrollmentHookAuth.md) |  | [optional]

## Example

```python
from flightctl.models.enrollment_hook_http_action import EnrollmentHookHttpAction

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookHttpAction from a JSON string
enrollment_hook_http_action_instance = EnrollmentHookHttpAction.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookHttpAction.to_json())

# convert the object into a dict
enrollment_hook_http_action_dict = enrollment_hook_http_action_instance.to_dict()
# create an instance of EnrollmentHookHttpAction from a dict
enrollment_hook_http_action_from_dict = EnrollmentHookHttpAction.from_dict(enrollment_hook_http_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
