# CheckRepositoryOciResult

Result of an OCI registry check (tag existence or image accessibility).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible** | **bool** | Whether the image or tag is accessible in the registry. | 
**error_code** | **int** | HTTP status code returned by the OCI registry when accessible is false. Absent when the failure is not an HTTP-level error (e.g. network timeout). | [optional] 
**error_message** | **str** | Error message describing why the image or tag is not accessible. | [optional] 

## Example

```python
from flightctl.models.check_repository_oci_result import CheckRepositoryOciResult

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRepositoryOciResult from a JSON string
check_repository_oci_result_instance = CheckRepositoryOciResult.from_json(json)
# print the JSON string representation of the object
print(CheckRepositoryOciResult.to_json())

# convert the object into a dict
check_repository_oci_result_dict = check_repository_oci_result_instance.to_dict()
# create an instance of CheckRepositoryOciResult from a dict
check_repository_oci_result_from_dict = CheckRepositoryOciResult.from_dict(check_repository_oci_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


