# RepositoryList

RepositoryList is a list of Repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[Repository]**](Repository.md) | List of repositories. | 

## Example

```python
from flightctl.models.repository_list import RepositoryList

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryList from a JSON string
repository_list_instance = RepositoryList.from_json(json)
# print the JSON string representation of the object
print(RepositoryList.to_json())

# convert the object into a dict
repository_list_dict = repository_list_instance.to_dict()
# create an instance of RepositoryList from a dict
repository_list_from_dict = RepositoryList.from_dict(repository_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


