# AapProviderSpec

AapProviderSpec describes an Ansible Automation Platform (AAP) provider configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**api_url** | **str** | The internal AAP API URL. | 
**authorization_url** | **str** | The OAuth2 authorization endpoint URL. | 
**token_url** | **str** | The OAuth2 token endpoint URL. | 
**client_id** | **str** | The OAuth2 client ID. | 
**client_secret** | **str** | The OAuth2 client secret. | 
**enabled** | **bool** | Whether this AAP provider is enabled. | [optional] [default to True]
**scopes** | **List[str]** | List of OAuth2 scopes to request. | 

## Example

```python
from flightctl.models.aap_provider_spec import AapProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AapProviderSpec from a JSON string
aap_provider_spec_instance = AapProviderSpec.from_json(json)
# print the JSON string representation of the object
print(AapProviderSpec.to_json())

# convert the object into a dict
aap_provider_spec_dict = aap_provider_spec_instance.to_dict()
# create an instance of AapProviderSpec from a dict
aap_provider_spec_from_dict = AapProviderSpec.from_dict(aap_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


