# PreEnrollmentActionResult

Result of a single executed pre-enrollment hook action, agent-populated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Path to the hook definition YAML that contained this action (for example /etc/flightctl/hooks.d/beforeenrolling/10-network.yaml). |
**exit_code** | **int** | Process exit code from the hook action. |
**output** | **str** | Redacted stdout/stderr from this action. The total size across all actions is capped at 4KiB. Secret patterns (PEM blocks, Bearer prefixes, known token env names) are redacted before persistence. | [optional]

## Example

```python
from flightctl.models.pre_enrollment_action_result import PreEnrollmentActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of PreEnrollmentActionResult from a JSON string
pre_enrollment_action_result_instance = PreEnrollmentActionResult.from_json(json)
# print the JSON string representation of the object
print(PreEnrollmentActionResult.to_json())

# convert the object into a dict
pre_enrollment_action_result_dict = pre_enrollment_action_result_instance.to_dict()
# create an instance of PreEnrollmentActionResult from a dict
pre_enrollment_action_result_from_dict = PreEnrollmentActionResult.from_dict(pre_enrollment_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
