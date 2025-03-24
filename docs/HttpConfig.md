# HttpConfig

Configuration for HTTP transport.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for auth with HTTP transport. | [optional] 
**password** | **str** | The password for auth with HTTP transport. | [optional] 
**tls_crt** | **str** | Base64 encoded TLS cert data. | [optional] 
**tls_key** | **str** | Base64 encoded TLS cert key. | [optional] 
**ca_crt** | **str** | Base64 encoded root CA. | [optional] 
**skip_server_verification** | **bool** | Skip remote server verification. | [optional] 
**token** | **str** | The token for auth with HTTP transport. | [optional] 

## Example

```python
from flightctl.models.http_config import HttpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConfig from a JSON string
http_config_instance = HttpConfig.from_json(json)
# print the JSON string representation of the object
print(HttpConfig.to_json())

# convert the object into a dict
http_config_dict = http_config_instance.to_dict()
# create an instance of HttpConfig from a dict
http_config_from_dict = HttpConfig.from_dict(http_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


