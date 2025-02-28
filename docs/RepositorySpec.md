# RepositorySpec

RepositorySpec describes a configuration repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The SSH Git repository URL to clone from. | 
**type** | [**RepoSpecType**](RepoSpecType.md) |  | 
**http_config** | [**HttpConfig**](HttpConfig.md) |  | 
**validation_suffix** | **str** | URL suffix used only for validating access to the repository. Users might use the URL field as a root URL to be used by config sources adding suffixes. This will help with the validation of the http endpoint. | [optional] 
**ssh_config** | [**SshConfig**](SshConfig.md) |  | 

## Example

```python
from flightctl.models.repository_spec import RepositorySpec

# TODO update the JSON string below
json = "{}"
# create an instance of RepositorySpec from a JSON string
repository_spec_instance = RepositorySpec.from_json(json)
# print the JSON string representation of the object
print(RepositorySpec.to_json())

# convert the object into a dict
repository_spec_dict = repository_spec_instance.to_dict()
# create an instance of RepositorySpec from a dict
repository_spec_from_dict = RepositorySpec.from_dict(repository_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


