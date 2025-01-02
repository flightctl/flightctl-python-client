# ConfigProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the config provider. | 
**git_ref** | [**GitConfigProviderSpecGitRef**](GitConfigProviderSpecGitRef.md) |  | 
**secret_ref** | [**KubernetesSecretProviderSpecSecretRef**](KubernetesSecretProviderSpecSecretRef.md) |  | 
**inline** | [**List[FileSpec]**](FileSpec.md) | A list of files to create on the device. | 
**http_ref** | [**HttpConfigProviderSpecHttpRef**](HttpConfigProviderSpecHttpRef.md) |  | 

## Example

```python
from flightctl.models.config_provider_spec import ConfigProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigProviderSpec from a JSON string
config_provider_spec_instance = ConfigProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ConfigProviderSpec.to_json())

# convert the object into a dict
config_provider_spec_dict = config_provider_spec_instance.to_dict()
# create an instance of ConfigProviderSpec from a dict
config_provider_spec_from_dict = ConfigProviderSpec.from_dict(config_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


