# EnrollmentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_service** | [**EnrollmentService**](EnrollmentService.md) |  | 

## Example

```python
from flightctl.models.enrollment_config import EnrollmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentConfig from a JSON string
enrollment_config_instance = EnrollmentConfig.from_json(json)
# print the JSON string representation of the object
print(EnrollmentConfig.to_json())

# convert the object into a dict
enrollment_config_dict = enrollment_config_instance.to_dict()
# create an instance of EnrollmentConfig from a dict
enrollment_config_from_dict = EnrollmentConfig.from_dict(enrollment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


