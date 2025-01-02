# EnrollmentServiceService

EnrollmentServiceService contains information about connecting to a Flight Control enrollment service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_authority_data** | **str** | CertificateAuthorityData contains PEM-encoded certificate authority certificates. | 
**server** | **str** | Server is the address of the Flight Control enrollment service (https://hostname:port). | 

## Example

```python
from flightctl.models.enrollment_service_service import EnrollmentServiceService

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentServiceService from a JSON string
enrollment_service_service_instance = EnrollmentServiceService.from_json(json)
# print the JSON string representation of the object
print(EnrollmentServiceService.to_json())

# convert the object into a dict
enrollment_service_service_dict = enrollment_service_service_instance.to_dict()
# create an instance of EnrollmentServiceService from a dict
enrollment_service_service_from_dict = EnrollmentServiceService.from_dict(enrollment_service_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


