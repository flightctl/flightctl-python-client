# EnrollmentService

EnrollmentService contains information about how to communicate with a Flight Control enrollment service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**EnrollmentServiceAuth**](EnrollmentServiceAuth.md) |  | 
**service** | [**EnrollmentServiceService**](EnrollmentServiceService.md) |  | 
**enrollment_ui_endpoint** | **str** | The URL of the UI that the agent uses to print the QR code and link for enrolling the device. | 

## Example

```python
from flightctl.models.enrollment_service import EnrollmentService

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentService from a JSON string
enrollment_service_instance = EnrollmentService.from_json(json)
# print the JSON string representation of the object
print(EnrollmentService.to_json())

# convert the object into a dict
enrollment_service_dict = enrollment_service_instance.to_dict()
# create an instance of EnrollmentService from a dict
enrollment_service_from_dict = EnrollmentService.from_dict(enrollment_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


