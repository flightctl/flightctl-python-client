# OciRepoSpec

OCI container registry specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry** | **str** | The OCI registry hostname, FQDN, or IP address with optional port (e.g., quay.io, registry.redhat.io, myregistry.com:5000, 192.168.1.1:5000, [::1]:5000). | 
**scheme** | **str** | URL scheme for connecting to the registry. | [optional] [default to 'https']
**type** | **str** | The repository type discriminator. | 
**access_mode** | **str** | Access mode for the registry: \&quot;Read\&quot; for read-only (pull), \&quot;ReadWrite\&quot; for read-write (pull and push). | [optional] [default to 'Read']
**oci_auth** | [**DockerAuth**](DockerAuth.md) |  | [optional] 
**ca_crt** | **str** | Base64 encoded root CA. | [optional] 
**skip_server_verification** | **bool** | Skip remote server verification. | [optional] 

## Example

```python
from flightctl.models.oci_repo_spec import OciRepoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OciRepoSpec from a JSON string
oci_repo_spec_instance = OciRepoSpec.from_json(json)
# print the JSON string representation of the object
print(OciRepoSpec.to_json())

# convert the object into a dict
oci_repo_spec_dict = oci_repo_spec_instance.to_dict()
# create an instance of OciRepoSpec from a dict
oci_repo_spec_from_dict = OciRepoSpec.from_dict(oci_repo_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


