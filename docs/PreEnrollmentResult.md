# PreEnrollmentResult

Result of pre-enrollment hook execution, agent-populated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether all pre-enrollment hooks completed with exit code 0. |
**actions** | [**List[PreEnrollmentActionResult]**](PreEnrollmentActionResult.md) | Per-action results in execution order. | [optional]

## Example

```python
from flightctl.models.pre_enrollment_result import PreEnrollmentResult

# TODO update the JSON string below
json = "{}"
# create an instance of PreEnrollmentResult from a JSON string
pre_enrollment_result_instance = PreEnrollmentResult.from_json(json)
# print the JSON string representation of the object
print(PreEnrollmentResult.to_json())

# convert the object into a dict
pre_enrollment_result_dict = pre_enrollment_result_instance.to_dict()
# create an instance of PreEnrollmentResult from a dict
pre_enrollment_result_from_dict = PreEnrollmentResult.from_dict(pre_enrollment_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
