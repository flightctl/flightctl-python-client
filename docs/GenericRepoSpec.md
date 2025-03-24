# GenericRepoSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The (possibly remote) repository URL. | 
**type** | [**RepoSpecType**](RepoSpecType.md) |  | 

## Example

```python
from flightctl.models.generic_repo_spec import GenericRepoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GenericRepoSpec from a JSON string
generic_repo_spec_instance = GenericRepoSpec.from_json(json)
# print the JSON string representation of the object
print(GenericRepoSpec.to_json())

# convert the object into a dict
generic_repo_spec_dict = generic_repo_spec_instance.to_dict()
# create an instance of GenericRepoSpec from a dict
generic_repo_spec_from_dict = GenericRepoSpec.from_dict(generic_repo_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


