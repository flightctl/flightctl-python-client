# EnrollmentRequestApproval

EnrollmentRequestApproval contains information about the approval of a device enrollment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **Dict[str, str]** | Labels to set on the device. If replaceLabels is false (default), labels are merged with agent-provided labels from the enrollment request. If replaceLabels is true, labels are used as the complete final set ignoring agent-provided labels. | [optional] 
**replace_labels** | **bool** | Controls whether labels are merged or replaced during approval. If false (default), labels are merged with agent-provided labels from the enrollment request. If true, labels are used as the complete final set and agent-provided labels are ignored. | [optional] [default to False]
**approved** | **bool** | Indicates whether the request has been approved. | 

## Example

```python
from flightctl.models.enrollment_request_approval import EnrollmentRequestApproval

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestApproval from a JSON string
enrollment_request_approval_instance = EnrollmentRequestApproval.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestApproval.to_json())

# convert the object into a dict
enrollment_request_approval_dict = enrollment_request_approval_instance.to_dict()
# create an instance of EnrollmentRequestApproval from a dict
enrollment_request_approval_from_dict = EnrollmentRequestApproval.from_dict(enrollment_request_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


