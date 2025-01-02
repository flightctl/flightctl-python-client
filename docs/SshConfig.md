# SshConfig

Configuration for SSH transport.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_private_key** | **str** | Base64 encoded private SSH key. | [optional] 
**private_key_passphrase** | **str** | The passphrase for sshPrivateKey. | [optional] 
**skip_server_verification** | **bool** | Skip remote server verification. | [optional] 

## Example

```python
from flightctl.models.ssh_config import SshConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SshConfig from a JSON string
ssh_config_instance = SshConfig.from_json(json)
# print the JSON string representation of the object
print(SshConfig.to_json())

# convert the object into a dict
ssh_config_dict = ssh_config_instance.to_dict()
# create an instance of SshConfig from a dict
ssh_config_from_dict = SshConfig.from_dict(ssh_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


