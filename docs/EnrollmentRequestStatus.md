# EnrollmentRequestStatus

EnrollmentRequestStatus represents information about the status of a EnrollmentRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The PEM-encoded signed certificate. | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | Current state of the EnrollmentRequest. | 
**approval** | [**EnrollmentRequestApprovalStatus**](EnrollmentRequestApprovalStatus.md) |  | [optional] 

## Example

```python
from flightctl.models.enrollment_request_status import EnrollmentRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestStatus from a JSON string
enrollment_request_status_instance = EnrollmentRequestStatus.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestStatus.to_json())

# convert the object into a dict
enrollment_request_status_dict = enrollment_request_status_instance.to_dict()
# create an instance of EnrollmentRequestStatus from a dict
enrollment_request_status_from_dict = EnrollmentRequestStatus.from_dict(enrollment_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


