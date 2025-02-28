# EnrollmentRequestApprovalStatus

EnrollmentRequestApprovalStatus represents information about the status of a device enrollment request approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **Dict[str, str]** | A set of labels to apply to the device. | [optional] 
**approved** | **bool** | Indicates whether the request has been approved. | 
**approved_by** | **str** | The name of the approver. | 
**approved_at** | **datetime** | The time at which the request was approved. | 

## Example

```python
from flightctl.models.enrollment_request_approval_status import EnrollmentRequestApprovalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestApprovalStatus from a JSON string
enrollment_request_approval_status_instance = EnrollmentRequestApprovalStatus.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestApprovalStatus.to_json())

# convert the object into a dict
enrollment_request_approval_status_dict = enrollment_request_approval_status_instance.to_dict()
# create an instance of EnrollmentRequestApprovalStatus from a dict
enrollment_request_approval_status_from_dict = EnrollmentRequestApprovalStatus.from_dict(enrollment_request_approval_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


