# AuthConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**providers** | [**List[AuthProvider]**](AuthProvider.md) | List of all available authentication providers. | [optional] 
**default_provider** | **str** | Name of the default authentication provider. | [optional] 
**organizations_enabled** | **bool** | Whether organizations are enabled for authentication. | [optional] 

## Example

```python
from flightctl.models.auth_config import AuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfig from a JSON string
auth_config_instance = AuthConfig.from_json(json)
# print the JSON string representation of the object
print(AuthConfig.to_json())

# convert the object into a dict
auth_config_dict = auth_config_instance.to_dict()
# create an instance of AuthConfig from a dict
auth_config_from_dict = AuthConfig.from_dict(auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


