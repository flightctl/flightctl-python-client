# SchemasStatus

Status is a return value for calls that don't return other objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**SchemasApiVersion**](SchemasApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**code** | **int** | Suggested HTTP return code for this status, 0 if not set. | 
**message** | **str** | A human-readable description of the status of this operation. | 
**reason** | **str** | A machine-readable description of why this operation is in the \&quot;Failure\&quot; status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. | 
**status** | **str** | Status of the operation. One of: \&quot;Success\&quot; or \&quot;Failure\&quot;. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. | 

## Example

```python
from flightctl.v1alpha1.models.schemas_status import SchemasStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasStatus from a JSON string
schemas_status_instance = SchemasStatus.from_json(json)
# print the JSON string representation of the object
print(SchemasStatus.to_json())

# convert the object into a dict
schemas_status_dict = schemas_status_instance.to_dict()
# create an instance of SchemasStatus from a dict
schemas_status_from_dict = SchemasStatus.from_dict(schemas_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


