# AuthPerUserOrganizationAssignment

AuthPerUserOrganizationAssignment creates a separate organization for each user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of organization assignment. | 
**organization_name_prefix** | **str** | The prefix for the user-specific organization name (e.g., \&quot;user-org-\&quot;). | [optional] [default to 'user-org-']
**organization_name_suffix** | **str** | The suffix for the user-specific organization name (e.g., \&quot;-org\&quot;). | [optional] [default to '']

## Example

```python
from flightctl.models.auth_per_user_organization_assignment import AuthPerUserOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPerUserOrganizationAssignment from a JSON string
auth_per_user_organization_assignment_instance = AuthPerUserOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthPerUserOrganizationAssignment.to_json())

# convert the object into a dict
auth_per_user_organization_assignment_dict = auth_per_user_organization_assignment_instance.to_dict()
# create an instance of AuthPerUserOrganizationAssignment from a dict
auth_per_user_organization_assignment_from_dict = AuthPerUserOrganizationAssignment.from_dict(auth_per_user_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


