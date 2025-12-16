# OIDCProviderSpec

OIDCProviderSpec describes an OIDC provider configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**issuer** | **str** | The OIDC issuer URL (e.g., https://accounts.google.com). | 
**client_id** | **str** | The OIDC client ID. | 
**client_secret** | **str** | The OIDC client secret. | 
**enabled** | **bool** | Whether this OIDC provider is enabled. | [optional] [default to True]
**scopes** | **List[str]** | List of OIDC scopes to request. | [optional] 
**organization_assignment** | [**AuthOrganizationAssignment**](AuthOrganizationAssignment.md) |  | 
**username_claim** | **List[str]** | JSON path to the username claim in the JWT token as an array of path segments (e.g., [\&quot;preferred_username\&quot;], [\&quot;email\&quot;], [\&quot;sub\&quot;]). | [optional] [default to ["preferred_username"]]
**role_assignment** | [**AuthRoleAssignment**](AuthRoleAssignment.md) |  | 

## Example

```python
from flightctl.models.oidc_provider_spec import OIDCProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCProviderSpec from a JSON string
oidc_provider_spec_instance = OIDCProviderSpec.from_json(json)
# print the JSON string representation of the object
print(OIDCProviderSpec.to_json())

# convert the object into a dict
oidc_provider_spec_dict = oidc_provider_spec_instance.to_dict()
# create an instance of OIDCProviderSpec from a dict
oidc_provider_spec_from_dict = OIDCProviderSpec.from_dict(oidc_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


