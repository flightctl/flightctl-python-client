# OAuth2Introspection

OAuth2Introspection defines the token introspection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The introspection type. | 
**url** | **str** | The GitHub API base URL. Defaults to https://api.github.com for GitHub.com, but can be customized for GitHub Enterprise Server. | [default to 'https://api.github.com']
**jwks_url** | **str** | The JWKS (JSON Web Key Set) endpoint URL for fetching public keys to validate JWT signatures. | 
**issuer** | **str** | Expected issuer claim value in the JWT. If not specified, uses the OAuth2ProviderSpec issuer. | [optional] 
**audience** | **List[str]** | Expected audience claim values in the JWT. If not specified, uses the OAuth2ProviderSpec clientId. | [optional] 

## Example

```python
from flightctl.models.o_auth2_introspection import OAuth2Introspection

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Introspection from a JSON string
o_auth2_introspection_instance = OAuth2Introspection.from_json(json)
# print the JSON string representation of the object
print(OAuth2Introspection.to_json())

# convert the object into a dict
o_auth2_introspection_dict = o_auth2_introspection_instance.to_dict()
# create an instance of OAuth2Introspection from a dict
o_auth2_introspection_from_dict = OAuth2Introspection.from_dict(o_auth2_introspection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


