# SshRepoSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The SSH Git repository URL to clone from. | 
**type** | [**RepoSpecType**](RepoSpecType.md) |  | 
**ssh_config** | [**SshConfig**](SshConfig.md) |  | 

## Example

```python
from flightctl.models.ssh_repo_spec import SshRepoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SshRepoSpec from a JSON string
ssh_repo_spec_instance = SshRepoSpec.from_json(json)
# print the JSON string representation of the object
print(SshRepoSpec.to_json())

# convert the object into a dict
ssh_repo_spec_dict = ssh_repo_spec_instance.to_dict()
# create an instance of SshRepoSpec from a dict
ssh_repo_spec_from_dict = SshRepoSpec.from_dict(ssh_repo_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


