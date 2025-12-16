# OrganizationSpec

OrganizationSpec describes an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name shown to users. | [optional] 
**external_id** | **str** | External ID of the organization. | [optional] 

## Example

```python
from flightctl.models.organization_spec import OrganizationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSpec from a JSON string
organization_spec_instance = OrganizationSpec.from_json(json)
# print the JSON string representation of the object
print(OrganizationSpec.to_json())

# convert the object into a dict
organization_spec_dict = organization_spec_instance.to_dict()
# create an instance of OrganizationSpec from a dict
organization_spec_from_dict = OrganizationSpec.from_dict(organization_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


