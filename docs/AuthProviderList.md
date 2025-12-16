# AuthProviderList

AuthProviderList is a list of auth providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[AuthProvider]**](AuthProvider.md) | List of auth providers. | 

## Example

```python
from flightctl.models.auth_provider_list import AuthProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProviderList from a JSON string
auth_provider_list_instance = AuthProviderList.from_json(json)
# print the JSON string representation of the object
print(AuthProviderList.to_json())

# convert the object into a dict
auth_provider_list_dict = auth_provider_list_instance.to_dict()
# create an instance of AuthProviderList from a dict
auth_provider_list_from_dict = AuthProviderList.from_dict(auth_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


