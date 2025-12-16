# AuthDynamicOrganizationAssignment

AuthDynamicOrganizationAssignment assigns users to organizations based on auth provider claims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of organization assignment. | 
**claim_path** | **List[str]** | The JSON path to the claim that contains the organization identifier (e.g., [\&quot;groups\&quot;, \&quot;0\&quot;] or [\&quot;custom\&quot;, \&quot;org\&quot;]). | 
**organization_name_prefix** | **str** | The prefix for the organization name (e.g., \&quot;org-\&quot;). | [optional] [default to '']
**organization_name_suffix** | **str** | The suffix for the organization name (e.g., \&quot;-org\&quot;). | [optional] [default to '']

## Example

```python
from flightctl.models.auth_dynamic_organization_assignment import AuthDynamicOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthDynamicOrganizationAssignment from a JSON string
auth_dynamic_organization_assignment_instance = AuthDynamicOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthDynamicOrganizationAssignment.to_json())

# convert the object into a dict
auth_dynamic_organization_assignment_dict = auth_dynamic_organization_assignment_instance.to_dict()
# create an instance of AuthDynamicOrganizationAssignment from a dict
auth_dynamic_organization_assignment_from_dict = AuthDynamicOrganizationAssignment.from_dict(auth_dynamic_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


