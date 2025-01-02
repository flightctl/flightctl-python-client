# EnrollmentRequestSpec

EnrollmentRequestSpec is a description of a EnrollmentRequest's target state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The PEM-encoded PKCS#10 certificate signing request. | 
**device_status** | [**DeviceStatus**](DeviceStatus.md) |  | [optional] 
**labels** | **Dict[str, str]** | A set of labels that the service will apply to this device when its enrollment is approved. | [optional] 

## Example

```python
from flightctl.models.enrollment_request_spec import EnrollmentRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestSpec from a JSON string
enrollment_request_spec_instance = EnrollmentRequestSpec.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestSpec.to_json())

# convert the object into a dict
enrollment_request_spec_dict = enrollment_request_spec_instance.to_dict()
# create an instance of EnrollmentRequestSpec from a dict
enrollment_request_spec_from_dict = EnrollmentRequestSpec.from_dict(enrollment_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


