# OrganizationList

OrganizationList is a list of Organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[Organization]**](Organization.md) | List of Organizations. | 

## Example

```python
from flightctl.models.organization_list import OrganizationList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationList from a JSON string
organization_list_instance = OrganizationList.from_json(json)
# print the JSON string representation of the object
print(OrganizationList.to_json())

# convert the object into a dict
organization_list_dict = organization_list_instance.to_dict()
# create an instance of OrganizationList from a dict
organization_list_from_dict = OrganizationList.from_dict(organization_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


