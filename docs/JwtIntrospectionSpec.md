# JwtIntrospectionSpec

JwtIntrospectionSpec defines token introspection using JWT validation with JWKS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The introspection type. | 
**jwks_url** | **str** | The JWKS (JSON Web Key Set) endpoint URL for fetching public keys to validate JWT signatures. | 
**issuer** | **str** | Expected issuer claim value in the JWT. If not specified, uses the OAuth2ProviderSpec issuer. | [optional] 
**audience** | **List[str]** | Expected audience claim values in the JWT. If not specified, uses the OAuth2ProviderSpec clientId. | [optional] 

## Example

```python
from flightctl.models.jwt_introspection_spec import JwtIntrospectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JwtIntrospectionSpec from a JSON string
jwt_introspection_spec_instance = JwtIntrospectionSpec.from_json(json)
# print the JSON string representation of the object
print(JwtIntrospectionSpec.to_json())

# convert the object into a dict
jwt_introspection_spec_dict = jwt_introspection_spec_instance.to_dict()
# create an instance of JwtIntrospectionSpec from a dict
jwt_introspection_spec_from_dict = JwtIntrospectionSpec.from_dict(jwt_introspection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


