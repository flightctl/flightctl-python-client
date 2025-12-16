# AuthOrganizationAssignment

AuthOrganizationAssignment defines how users from this auth provider are assigned to organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of organization assignment. | 
**organization_name** | **str** | The name of the organization where all users will be assigned. | 
**claim_path** | **List[str]** | The JSON path to the claim that contains the organization identifier (e.g., [\&quot;groups\&quot;, \&quot;0\&quot;] or [\&quot;custom\&quot;, \&quot;org\&quot;]). | 
**organization_name_prefix** | **str** | The prefix for the user-specific organization name (e.g., \&quot;user-org-\&quot;). | [optional] [default to 'user-org-']
**organization_name_suffix** | **str** | The suffix for the user-specific organization name (e.g., \&quot;-org\&quot;). | [optional] [default to '']

## Example

```python
from flightctl.models.auth_organization_assignment import AuthOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthOrganizationAssignment from a JSON string
auth_organization_assignment_instance = AuthOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthOrganizationAssignment.to_json())

# convert the object into a dict
auth_organization_assignment_dict = auth_organization_assignment_instance.to_dict()
# create an instance of AuthOrganizationAssignment from a dict
auth_organization_assignment_from_dict = AuthOrganizationAssignment.from_dict(auth_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


