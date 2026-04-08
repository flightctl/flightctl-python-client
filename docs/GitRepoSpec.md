# GitRepoSpec

Git repository specification. Supports no auth (public repos), HTTP/HTTPS auth, or SSH auth.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The Git repository URL to clone from. | 
**type** | **str** | The repository type discriminator. | 
**http_config** | [**HttpConfig**](HttpConfig.md) |  | [optional] 
**ssh_config** | [**SshConfig**](SshConfig.md) |  | [optional] 

## Example

```python
from flightctl.models.git_repo_spec import GitRepoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GitRepoSpec from a JSON string
git_repo_spec_instance = GitRepoSpec.from_json(json)
# print the JSON string representation of the object
print(GitRepoSpec.to_json())

# convert the object into a dict
git_repo_spec_dict = git_repo_spec_instance.to_dict()
# create an instance of GitRepoSpec from a dict
git_repo_spec_from_dict = GitRepoSpec.from_dict(git_repo_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


