# EnrollmentHookRetryPolicy

Retry policy for an enrollment hook action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | Maximum number of retry attempts. Defaults to 5, max 20. | [optional]
**backoff_policy** | **str** | Backoff strategy (e.g. \&quot;exponential\&quot;). Defaults to \&quot;exponential\&quot;. | [optional]
**backoff_delay** | **str** | Initial backoff delay duration (e.g. \&quot;2s\&quot;). Defaults to \&quot;2s\&quot;. | [optional]
**max_backoff** | **str** | Maximum backoff duration (e.g. \&quot;2m\&quot;). Defaults to \&quot;2m\&quot;. | [optional]
**deadline** | **str** | Overall deadline for all retry attempts (e.g. \&quot;10m\&quot;). Defaults to \&quot;10m\&quot;. | [optional]

## Example

```python
from flightctl.models.enrollment_hook_retry_policy import EnrollmentHookRetryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookRetryPolicy from a JSON string
enrollment_hook_retry_policy_instance = EnrollmentHookRetryPolicy.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookRetryPolicy.to_json())

# convert the object into a dict
enrollment_hook_retry_policy_dict = enrollment_hook_retry_policy_instance.to_dict()
# create an instance of EnrollmentHookRetryPolicy from a dict
enrollment_hook_retry_policy_from_dict = EnrollmentHookRetryPolicy.from_dict(enrollment_hook_retry_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
