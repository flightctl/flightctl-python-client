# Permission

A permission defining allowed operations on a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | The resource (e.g., \&quot;devices\&quot;, \&quot;fleets\&quot;, \&quot;*\&quot; for all resources). | 
**operations** | **List[str]** | List of allowed operations (e.g., \&quot;get\&quot;, \&quot;list\&quot;, \&quot;create\&quot;, \&quot;update\&quot;, \&quot;patch\&quot;, \&quot;delete\&quot;, \&quot;*\&quot; for all operations). | 

## Example

```python
from flightctl.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_from_dict = Permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


