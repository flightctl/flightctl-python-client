# GitConfigProviderSpecGitRef

The reference to a Git configuration server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The name of the Repository resource. | 
**target_revision** | **str** | The revision to use from the Repository. | 
**path** | **str** | The path to the config in the Repository. | 
**mount_path** | **str** | Path in the device&#39;s file system at which the repository&#39;s path should be mounted. | [optional] [default to '/']

## Example

```python
from flightctl.models.git_config_provider_spec_git_ref import GitConfigProviderSpecGitRef

# TODO update the JSON string below
json = "{}"
# create an instance of GitConfigProviderSpecGitRef from a JSON string
git_config_provider_spec_git_ref_instance = GitConfigProviderSpecGitRef.from_json(json)
# print the JSON string representation of the object
print(GitConfigProviderSpecGitRef.to_json())

# convert the object into a dict
git_config_provider_spec_git_ref_dict = git_config_provider_spec_git_ref_instance.to_dict()
# create an instance of GitConfigProviderSpecGitRef from a dict
git_config_provider_spec_git_ref_from_dict = GitConfigProviderSpecGitRef.from_dict(git_config_provider_spec_git_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


