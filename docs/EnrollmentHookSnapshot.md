# EnrollmentHookSnapshot

Immutable non-secret copy of EnrollmentHookPolicy fields captured at approval time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_policy** | [**FailurePolicyType**](FailurePolicyType.md) |  |
**control_plane_actions** | [**List[EnrollmentHookSnapshotAction]**](EnrollmentHookSnapshotAction.md) | Non-secret copies of control-plane actions from the policy at approval time. | [optional]

## Example

```python
from flightctl.models.enrollment_hook_snapshot import EnrollmentHookSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentHookSnapshot from a JSON string
enrollment_hook_snapshot_instance = EnrollmentHookSnapshot.from_json(json)
# print the JSON string representation of the object
print(EnrollmentHookSnapshot.to_json())

# convert the object into a dict
enrollment_hook_snapshot_dict = enrollment_hook_snapshot_instance.to_dict()
# create an instance of EnrollmentHookSnapshot from a dict
enrollment_hook_snapshot_from_dict = EnrollmentHookSnapshot.from_dict(enrollment_hook_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
