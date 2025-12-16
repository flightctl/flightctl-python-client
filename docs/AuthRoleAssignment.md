# AuthRoleAssignment

AuthRoleAssignment defines how roles are assigned to users from this auth provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of role assignment. | 
**roles** | **List[str]** | The list of role names to assign to all users. | 
**claim_path** | **List[str]** | The JSON path to the role/group claim (e.g., [\&quot;groups\&quot;], [\&quot;roles\&quot;], [\&quot;realm_access\&quot;, \&quot;roles\&quot;]). | 
**separator** | **str** | Separator for org:role format (default &#39;:&#39;). Roles containing the separator are split into organization-scoped roles. Roles without separator are global and apply to all organizations. | [optional] [default to ':']

## Example

```python
from flightctl.models.auth_role_assignment import AuthRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRoleAssignment from a JSON string
auth_role_assignment_instance = AuthRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthRoleAssignment.to_json())

# convert the object into a dict
auth_role_assignment_dict = auth_role_assignment_instance.to_dict()
# create an instance of AuthRoleAssignment from a dict
auth_role_assignment_from_dict = AuthRoleAssignment.from_dict(auth_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


