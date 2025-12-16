# AuthStaticRoleAssignment

AuthStaticRoleAssignment assigns a static set of roles to all users from this auth provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of role assignment. | 
**roles** | **List[str]** | The list of role names to assign to all users. | 

## Example

```python
from flightctl.models.auth_static_role_assignment import AuthStaticRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthStaticRoleAssignment from a JSON string
auth_static_role_assignment_instance = AuthStaticRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthStaticRoleAssignment.to_json())

# convert the object into a dict
auth_static_role_assignment_dict = auth_static_role_assignment_instance.to_dict()
# create an instance of AuthStaticRoleAssignment from a dict
auth_static_role_assignment_from_dict = AuthStaticRoleAssignment.from_dict(auth_static_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


