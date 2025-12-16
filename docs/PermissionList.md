# PermissionList

List of available permissions for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[Permission]**](Permission.md) | List of permissions available to the user. | 

## Example

```python
from flightctl.models.permission_list import PermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionList from a JSON string
permission_list_instance = PermissionList.from_json(json)
# print the JSON string representation of the object
print(PermissionList.to_json())

# convert the object into a dict
permission_list_dict = permission_list_instance.to_dict()
# create an instance of PermissionList from a dict
permission_list_from_dict = PermissionList.from_dict(permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


