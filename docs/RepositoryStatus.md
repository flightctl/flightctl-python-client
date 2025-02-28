# RepositoryStatus

RepositoryStatus represents information about the status of a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[Condition]**](Condition.md) | Current state of the repository. | 

## Example

```python
from flightctl.models.repository_status import RepositoryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryStatus from a JSON string
repository_status_instance = RepositoryStatus.from_json(json)
# print the JSON string representation of the object
print(RepositoryStatus.to_json())

# convert the object into a dict
repository_status_dict = repository_status_instance.to_dict()
# create an instance of RepositoryStatus from a dict
repository_status_from_dict = RepositoryStatus.from_dict(repository_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


