# AuthStaticOrganizationAssignment

AuthStaticOrganizationAssignment assigns all users from this auth provider to a single static organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of organization assignment. | 
**organization_name** | **str** | The name of the organization where all users will be assigned. | 

## Example

```python
from flightctl.models.auth_static_organization_assignment import AuthStaticOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthStaticOrganizationAssignment from a JSON string
auth_static_organization_assignment_instance = AuthStaticOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(AuthStaticOrganizationAssignment.to_json())

# convert the object into a dict
auth_static_organization_assignment_dict = auth_static_organization_assignment_instance.to_dict()
# create an instance of AuthStaticOrganizationAssignment from a dict
auth_static_organization_assignment_from_dict = AuthStaticOrganizationAssignment.from_dict(auth_static_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


