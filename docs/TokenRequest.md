# TokenRequest

OAuth2 token request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | OAuth2 grant type. | 
**client_id** | **str** | OAuth2 client identifier. | 
**refresh_token** | **str** | Refresh token for refresh_token grant. | [optional] 
**code** | **str** | Authorization code for authorization_code grant. | [optional] 
**scope** | **str** | OAuth2 scope. | [optional] 
**code_verifier** | **str** | PKCE code verifier. | [optional] 
**redirect_uri** | **str** | OAuth2 redirect URI (required for authorization_code grant if included in authorization request). | [optional] 

## Example

```python
from flightctl.models.token_request import TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequest from a JSON string
token_request_instance = TokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRequest.to_json())

# convert the object into a dict
token_request_dict = token_request_instance.to_dict()
# create an instance of TokenRequest from a dict
token_request_from_dict = TokenRequest.from_dict(token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


