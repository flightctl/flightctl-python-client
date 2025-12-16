# OAuth2ProviderSpec

OAuth2ProviderSpec describes an OAuth2 provider configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**issuer** | **str** | The OAuth2 issuer identifier (used for issuer identification in tokens). | [optional] 
**authorization_url** | **str** | The OAuth2 authorization endpoint URL. | 
**token_url** | **str** | The OAuth2 token endpoint URL. | 
**userinfo_url** | **str** | The OAuth2 userinfo endpoint URL. | 
**client_id** | **str** | The OAuth2 client ID. | 
**client_secret** | **str** | The OAuth2 client secret. | 
**enabled** | **bool** | Whether this OAuth2 provider is enabled. | [optional] [default to True]
**scopes** | **List[str]** | List of OAuth2 scopes to request. | [optional] 
**organization_assignment** | [**AuthOrganizationAssignment**](AuthOrganizationAssignment.md) |  | 
**username_claim** | **List[str]** | JSON path to the username claim in the userinfo response as an array of path segments (e.g., [\&quot;preferred_username\&quot;], [\&quot;email\&quot;], [\&quot;sub\&quot;]). | [optional] [default to ["preferred_username"]]
**role_assignment** | [**AuthRoleAssignment**](AuthRoleAssignment.md) |  | 
**introspection** | [**OAuth2Introspection**](OAuth2Introspection.md) |  | [optional] 

## Example

```python
from flightctl.models.o_auth2_provider_spec import OAuth2ProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ProviderSpec from a JSON string
o_auth2_provider_spec_instance = OAuth2ProviderSpec.from_json(json)
# print the JSON string representation of the object
print(OAuth2ProviderSpec.to_json())

# convert the object into a dict
o_auth2_provider_spec_dict = o_auth2_provider_spec_instance.to_dict()
# create an instance of OAuth2ProviderSpec from a dict
o_auth2_provider_spec_from_dict = OAuth2ProviderSpec.from_dict(o_auth2_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


