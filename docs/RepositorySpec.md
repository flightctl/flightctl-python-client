# RepositorySpec

RepositorySpec describes a configuration repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTP URL to call. | 
**type** | **str** | The repository type discriminator. | 
**http_config** | [**HttpConfig**](HttpConfig.md) |  | [optional] 
**ssh_config** | [**SshConfig**](SshConfig.md) |  | [optional] 
**validation_suffix** | **str** | URL suffix used only for validating access to the repository. Users might use the URL field as a root URL to be used by config sources adding suffixes. This will help with the validation of the http endpoint. | [optional] 
**registry** | **str** | The OCI registry hostname, FQDN, or IP address with optional port (e.g., quay.io, registry.redhat.io, myregistry.com:5000, 192.168.1.1:5000, [::1]:5000). | 
**scheme** | **str** | URL scheme for connecting to the registry. | [optional] [default to 'https']
**access_mode** | **str** | Access mode for the registry: \&quot;Read\&quot; for read-only (pull), \&quot;ReadWrite\&quot; for read-write (pull and push). | [optional] [default to 'Read']
**oci_auth** | [**DockerAuth**](DockerAuth.md) |  | [optional] 
**ca_crt** | **str** | Base64 encoded root CA. | [optional] 
**skip_server_verification** | **bool** | Skip remote server verification. | [optional] 

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


