# GitConfigProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the config provider. | 
**git_ref** | [**GitConfigProviderSpecGitRef**](GitConfigProviderSpecGitRef.md) |  | 

## Example

```python
from flightctl.models.git_config_provider_spec import GitConfigProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GitConfigProviderSpec from a JSON string
git_config_provider_spec_instance = GitConfigProviderSpec.from_json(json)
# print the JSON string representation of the object
print(GitConfigProviderSpec.to_json())

# convert the object into a dict
git_config_provider_spec_dict = git_config_provider_spec_instance.to_dict()
# create an instance of GitConfigProviderSpec from a dict
git_config_provider_spec_from_dict = GitConfigProviderSpec.from_dict(git_config_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


