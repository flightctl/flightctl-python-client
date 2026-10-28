# EnrollmentHookSnapshotAction

Non-secret copy of an enrollment hook HTTP action. Excludes auth/bearerToken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Original action index in the policy. |
**url** | **str** | The HTTPS URL to call. |
**timeout** | **str** | Timeout duration (e.g. \&quot;30s\&quot;). | [optional]
**retry** | [**EnrollmentHookRetryPolicy**](EnrollmentHookRetryPolicy.md) |  | [optional]

## Example

```python
from flightctl.models.enrollment_hook_snapshot_action import EnrollmentHookSnapshotAction

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookSnapshotAction from a JSON string
enrollment_hook_snapshot_action_instance = EnrollmentHookSnapshotAction.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookSnapshotAction.to_json())

# convert the object into a dict
enrollment_hook_snapshot_action_dict = enrollment_hook_snapshot_action_instance.to_dict()
# create an instance of EnrollmentHookSnapshotAction from a dict
enrollment_hook_snapshot_action_from_dict = EnrollmentHookSnapshotAction.from_dict(enrollment_hook_snapshot_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
