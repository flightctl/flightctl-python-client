# EnrollmentRequest

EnrollmentRequest represents a request for approval to enroll a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**EnrollmentRequestSpec**](EnrollmentRequestSpec.md) |  | 
**status** | [**EnrollmentRequestStatus**](EnrollmentRequestStatus.md) |  | [optional] 

## Example

```python
from flightctl.models.enrollment_request import EnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequest from a JSON string
enrollment_request_instance = EnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequest.to_json())

# convert the object into a dict
enrollment_request_dict = enrollment_request_instance.to_dict()
# create an instance of EnrollmentRequest from a dict
enrollment_request_from_dict = EnrollmentRequest.from_dict(enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


